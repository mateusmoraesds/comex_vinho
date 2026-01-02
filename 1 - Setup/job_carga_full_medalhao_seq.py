"""
Arquitetura de Orquestração Orientada a Metadados

Este job utiliza uma abordagem de orquestração orientada a metadados
(metadata-driven), onde cada camada da arquitetura medalhão (Bronze,
Silver e Gold) possui:

- Um arquivo JSON responsável por cadastrar os notebooks de criação e
  transformação das tabelas;
- Um notebook orquestrador, que lê esse JSON como parâmetro e decide
  dinamicamente quais notebooks devem ser executados;
- DataFrames internos que armazenam metadados de execução (status,
  tempo, camada, erro, etc.), os quais são persistidos em tabelas no
  Unity Catalog para fins de governança e observabilidade.

Embora visualmente o Databricks apresente este fluxo como um único Job,
a dependência entre as cargas é lógica e orientada por metadados, e não
acoplada tecnicamente. Cada notebook representa uma unidade lógica
independente, permitindo controle, rastreabilidade e evolução do
pipeline sem hard-code de dependências.
"""

# Importação da classe Job do Databricks Asset Bundles (DAB)
# Permite definir Jobs como código versionável em Git
from databricks.bundles.jobs import Job


# ----------------------------------------------------------------------------
# Definição do Job Databricks
# ----------------------------------------------------------------------------
Carga_Full_Todas_Camadas_Seq = Job.from_dict(
    {
        # Nome do Job exibido no Databricks
        "name": "Carga_Full_Todas_Camadas_Seq",

        # --------------------------------------------------------------------
        # Agendamento do Job
        # --------------------------------------------------------------------
        "schedule": {
            # Expressão Quartz Cron:
            # Executa diariamente às 06:30:05
            "quartz_cron_expression": "5 30 6 * * ?",
            "timezone_id": "America/Sao_Paulo",
            "pause_status": "UNPAUSED",
        },

        # --------------------------------------------------------------------
        # Definição das Tasks
        # --------------------------------------------------------------------
        "tasks": [
            # ----------------------
            # Task Bronze
            # ----------------------
            {
                "task_key": "Roda_Carga_Bronze",
                "notebook_task": {
                    "notebook_path": (
                        "/Workspace/Users/"
                        "mateusmoraesds@gmail.com/"
                        "comex_vinho/1 - Setup/Orquestração/"
                        "Orquestrador_Cargas_Bronze"
                    ),
                    "source": "WORKSPACE",
                },
            },

            # ----------------------
            # Task Silver
            # ----------------------
            {
                "task_key": "Roda_Carga_Silver",
                "depends_on": [
                    {"task_key": "Roda_Carga_Bronze"}
                ],
                "notebook_task": {
                    "notebook_path": (
                        "/Workspace/Users/"
                        "mateusmoraesds@gmail.com/"
                        "comex_vinho/1 - Setup/Orquestração/"
                        "Orquestrador_Cargas_Silver"
                    ),
                    "source": "WORKSPACE",
                },
                # Timeout de segurança (20 minutos)
                "timeout_seconds": 1200,
            },

            # ----------------------
            # Task Gold
            # ----------------------
            {
                "task_key": "Roda_Carga_Gold",
                "depends_on": [
                    {"task_key": "Roda_Carga_Silver"}
                ],
                "notebook_task": {
                    "notebook_path": (
                        "/Workspace/Users/"
                        "mateusmoraesds@gmail.com/"
                        "comex_vinho/1 - Setup/Orquestração/"
                        "Orquestrador_Cargas_Gold"
                    ),
                    "source": "WORKSPACE",
                },
            },
        ],

        # --------------------------------------------------------------------
        # Tags para organização e governança
        # --------------------------------------------------------------------
        "tags": {
            "projeto": "comex_vinho",
            "arquitetura": "medalhao",
            "tipo_carga": "full",
            "ambiente": "estudos",
        },

        # --------------------------------------------------------------------
        # Queue habilitada (evita concorrência excessiva)
        # --------------------------------------------------------------------
        "queue": {
            "enabled": True,
        },

        # --------------------------------------------------------------------
        # Ambientes (obrigatório no DAB)
        # --------------------------------------------------------------------
        "environments": [
            {
                "environment_key": "Default",
                "spec": {
                    "environment_version": "4",
                },
            }
        ],

        # --------------------------------------------------------------------
        # Perfil de performance
        # --------------------------------------------------------------------
        "performance_target": "PERFORMANCE_OPTIMIZED",
    }
)
