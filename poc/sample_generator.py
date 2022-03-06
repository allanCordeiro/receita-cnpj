import os
import apache_beam as beam
from apache_beam.io.textio import ReadFromText, WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.coders import Coder

'''
Motivação: Os arquivos disponíveis são muitos, e muito grandes. A idéia foi gerar um sample
com os dados maiores (estabelecimentos, empresas, socios e opção pelo simples). 
'''

class ISOCoder(Coder):
    """A coder used for reading and writing strings as ISO-8859-1."""
    def encode(self, value):
        return value.encode('iso-8859-1')
    def decode(self, value):
        return value.decode('iso-8859-1')
    def is_deterministic(self):
        return True    

CURRENT_DIR = os.path.abspath(os.getcwd())
ds_empresas = f"{CURRENT_DIR}/../datalake/bronze/sample/SAMPLE_EMPRECSV"
ds_estabele = f"{CURRENT_DIR}/../datalake/bronze/sample/K3241.K03200Y0.D20108.ESTABELE"
ds_simples = f"{CURRENT_DIR}/../datalake/bronze/sample/F.K03200$W.SIMPLES.CSV.D20108"
ds_socios = f"{CURRENT_DIR}/../datalake/bronze/sample/K3241.K03200Y0.D20108.SOCIOCSV"


def start_pipelines():
    with beam.Pipeline() as pipeline:
        pl_empresas = (
            pipeline
            | "Open empresas file" >> ReadFromText(ds_empresas)
            | "convert to list" >> beam.Map(lambda record : record.split(";"))
            | "get CNPJ base info" >> beam.Map(lambda record: record[0])
            #| "Show data" >> beam.Map(print)

        )

        pl_estabelecimentos = (
            pipeline
            | "Open estabele's file" >> ReadFromText(ds_estabele, coder=ISOCoder())
            | "convert estabele to list" >> beam.Map(lambda record : record.split(";"))
            | 'filtering by cnpjs from empresas' >> beam.Filter(
                lambda record,
                pl_empresas: record[0] in pl_empresas,
                pl_empresas = beam.pvalue.AsIter(pl_empresas)
            )
            | "Convert estabele to csv" >> beam.Map(lambda record : f";".join(record))
            | "create estabele sample" >> WriteToText(
                f"{CURRENT_DIR}/../datalake/bronze/sample/SAMPLE_ESTABELE"
            )
        )
        
        pl_simples = (
            pipeline
            | "Open simples's file" >> ReadFromText(ds_simples, coder=ISOCoder())
            | "convert simples to list" >> beam.Map(lambda record : record.split(";"))
            | 'filtering by cnpjs from empresas' >> beam.Filter(
                lambda record,
                pl_empresas: record[0] in pl_empresas,
                pl_empresas = beam.pvalue.AsIter(pl_empresas)
            )
            | "Convert simples to csv" >> beam.Map(lambda record : f";".join(record))
            | "create simples sample" >> WriteToText(
                f"{CURRENT_DIR}/../datalake/bronze/sample/SAMPLE_SIMPLES.CSV.DS20108"
            )
        )
        
        pl_socios = (
            pipeline
            | "Open socio's file" >> ReadFromText(ds_socios, coder=ISOCoder())
            | "convert socios to list" >> beam.Map(lambda record : record.split(";"))
            | 'filtering by cnpjs from empresas' >> beam.Filter(
                lambda record,
                pl_empresas: record[0] in pl_empresas,
                pl_empresas = beam.pvalue.AsIter(pl_empresas)
            )
            | "Convert socios to csv" >> beam.Map(lambda record : f";".join(record))
            | "create socios sample" >> WriteToText(
                f"{CURRENT_DIR}/../datalake/bronze/sample/SAMPLE_D20108.SOCIOCSV"
            )
        )
        


if __name__=="__main__":
    start_pipelines()
    
    
