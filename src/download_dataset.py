import kaggle as kg


kg.api.authenticate()

kg.api.dataset_download_files('datahackers/state-of-data-brazil-2023',\
path=r'C:\Users\igors\Documentos\Estudo_python\Data Hackers\DataHarckers_2023\Data'\
, unzip=True)