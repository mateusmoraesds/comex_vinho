# comex_vinho: Análise de Comércio Exterior de Vinhos

Análise sobre vendas e exportação de vinhos de uma empresa localizada no Rio Grande do Sul (RS). Este projeto implementa um pipeline de dados completo, seguindo a arquitetura Medallion, para transformar dados brutos em informações estratégicas prontas para consumo e análise de negócios.

## 1. Arquitetura do Projeto

O projeto adota a **Arquitetura Medallion** (Bronze, Silver, Gold), um padrão de design de data lakehouse que garante a qualidade e a confiabilidade dos dados em cada estágio do pipeline. A implementação é realizada através de Notebooks utilizando a plataforma Databricks por meio de tecnologias de processamento distribuído (**Apache Spark** e **Delta Lake**).

| Camada | Propósito | Características |

| **Bronze** | Ingestão de dados brutos (Raw Data). | Dados originais, sem transformações, mantendo o histórico e a fidelidade da fonte. |
| **Silver** | Limpeza e Enriquecimento (Cleaned/Filtered Data). | Aplicação de regras de qualidade, filtragem, padronização e enriquecimento. Os dados estão prontos para análises mais detalhadas. |
| **Gold** | Dados de Negócio (Business-Ready Data). | Dados agregados, sumarizados e modelados (Data Marts/Dimensional) para consumo direto por ferramentas de BI e relatórios. |

## 2. Estrutura de Diretórios

A organização do repositório reflete as etapas do pipeline de dados, desde a configuração inicial até a camada de consumo final.

| Diretório | Conteúdo | Objetivo |
| :--- | :--- | :--- |
| `1 - Setup` | Arquivos de configuração, criação de schemas e orquestração. | Preparação do ambiente e definição da lógica de execução do pipeline. |
| `2 - Bronze` | Notebooks de ingestão de dados brutos. | Carregamento inicial dos dados de diversas fontes para o Data Lake. |
| `3 - Silver` | Notebooks de transformação e limpeza de dados. | Processamento dos dados brutos para garantir qualidade e consistência. |
| `4 - Gold` | Notebooks de modelagem e agregação de dados. | Criação de Data Marts e tabelas dimensionais para consumo de BI. |

### 2.1. Detalhes da Camada de Setup (`1 - Setup`)

Esta camada é crucial para a inicialização do ambiente e a automação do fluxo de trabalho.

*   **`Criação de Schemas e Tabelas.ipynb`**: Notebook responsável por definir a estrutura inicial do Data Lakehouse, criando os schemas e as tabelas de destino nas camadas Bronze, Silver e Gold.
*   **`Ingestao_bibliotecas_padrao.ipynb`**: Contém a lógica para a instalação e importação das bibliotecas Python necessárias para a execução dos *notebooks* do projeto (e.g., Spark, Delta Lake, Pandas).
*   **`JSON Orquestradores/`**: Contém arquivos JSON que definem a sequência e os parâmetros de execução dos *notebooks* em cada camada (Bronze, Silver, Gold), incluindo versões para execução paralela.
*   **`Orquestração/`**: Contém os *notebooks* mestres (`Orquestrador_Cargas_...ipynb`) que leem os arquivos JSON e executam as cargas de dados de forma orquestrada, garantindo a ordem correta das transformações.

### 2.2. Detalhes da Camada Bronze (`2 - Bronze`)

Os *notebooks* nesta camada são responsáveis pela ingestão dos dados brutos.

| Notebook | Descrição da Ingestão |
| :--- | :--- |
| `bronze_ExpEspumantes.ipynb` | Exportação de Espumantes. |
| `bronze_ExpSuco.ipynb` | Exportação de Suco. |
| `bronze_ExpUva.ipynb` | Exportação de Uva. |
| `bronze_ExpVinho.ipynb` | Exportação de Vinho. |
| `bronze_ProcessaAmericanas.ipynb` | Processamento de Vinhos Americanos. |
| `bronze_ProcessaMesa.ipynb` | Processamento de Vinhos de Mesa. |
| `bronze_ProcessaViniferas.ipynb` | Processamento de Vinhos Viníferas. |
| `bronze_Producao.ipynb` | Dados de Produção. |
| `bronze_comercio.ipynb` | Dados de Comercialização. |
| `bronze_dados_demograficos.ipynb` | Dados Demográficos. |

### 2.3. Detalhes da Camada Silver (`3 - Silver`)

Nesta camada, os dados brutos são limpos, padronizados e enriquecidos.

| Notebook | Descrição da Transformação |
| :--- | :--- |
| `silver_Comercio.ipynb` | Limpeza e enriquecimento dos dados de Comercialização. |
| `silver_ExpEspumantes.ipynb` | Limpeza e enriquecimento dos dados de Exportação de Espumantes. |
| `silver_ExpSuco.ipynb` | Limpeza e enriquecimento dos dados de Exportação de Suco. |
| `silver_ExpUva.ipynb` | Limpeza e enriquecimento dos dados de Exportação de Uva. |
| `silver_ExpVinhos.ipynb` | Limpeza e enriquecimento dos dados de Exportação de Vinhos. |
| `silver_ProcessaAmericanas.ipynb` | Limpeza e enriquecimento dos dados de Vinhos Americanos. |
| `silver_ProcessaMesa.ipynb` | Limpeza e enriquecimento dos dados de Vinhos de Mesa. |
| `silver_ProcessaViniferas.ipynb` | Limpeza e enriquecimento dos dados de Vinhos Viníferas. |
| `silver_Producao.ipynb` | Limpeza e enriquecimento dos dados de Produção. |
| `silver_dados_demograficos.ipynb` | Limpeza e enriquecimento dos dados Demográficos. |

### 2.4. Detalhes da Camada Gold (`4 - Gold`)

A camada Gold contém os dados finais, prontos para análise e consumo de negócios.

| Notebook | Descrição da Modelagem |
| :--- | :--- |
| `gold_Comercializacao.ipynb` | Criação de um Data Mart para análise de Comercialização. |
| `gold_Dados_demograficos.ipynb` | Criação de um Data Mart para análise de Dados Demográficos. |
| `gold_Exportacao_Vinhos.ipynb` | Criação de um Data Mart para análise de Exportação de Vinhos. |
| `gold_dim_paises.ipynb` | Criação da tabela dimensional de Países. |
| `gold_producao.ipynb` | Criação de um Data Mart para análise de Produção. |


Dúvidas, fico a disposição para contato na minha página do linkedin
linkedin.com/mateusmoraesds/
