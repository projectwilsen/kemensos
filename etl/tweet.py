from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv()
from supabase.client import Client, create_client

groq_api_key = os.getenv("GROQ_API_KEY")
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")

supabase_client = create_client(supabase_url, supabase_key)

model = ChatGroq(model="llama3-70b-8192",groq_api_key = groq_api_key)
data = pd.read_csv('sentimen_sembako.csv', sep = ';')

def concatenate_text(df, category, threshold=100, sample_frac=0.2, random_state=1):
    filtered_df = df.query(f'category == {category}')
    if len(filtered_df) > threshold:
        return filtered_df.sample(frac=sample_frac, random_state=random_state)['full_text'].str.cat(sep=' ')
    else:
        return filtered_df['full_text'].str.cat(sep=' ')

def summarize(tweets, sentimen):
    if sentimen == "positif":
        contoh = "apresiasi, pujian"
    elif sentimen == "negatif":
        contoh = "keluhan, kritik"

    template = """
    List poin - poin {sentimen} seperti {contoh} apa saja yang dikatakan oleh masyarakat dalam tweet ini dalam Bahasa Indonesia {tweets}
    Hanya dalam bahasa Indonesia. Tidak perlu menambahkan penjelasan di awal
    """

    prompt = ChatPromptTemplate.from_template(template = template)
    output_parser = StrOutputParser()

    chain = prompt | model | output_parser

    result = chain.invoke({"tweets": tweets, "sentimen":sentimen, "contoh":contoh})
    return result

pos = concatenate_text(data, 1.0)
neg = concatenate_text(data, 0.0)

pos_summary = summarize(pos,'positif')
neg_summary = summarize(neg,'negatif')

nama_program = data['jenis_program'][0]

if nama_program == 'Program Keluarga Harapan (PKH)':
    id = 1
elif nama_program == 'Bantuan Pangan Non-Tunai (BPNT)':
    id = 2
elif nama_program == 'Program Bantuan Sosial (Bansos)':
    id = 3
elif nama_program == 'Bantuan Langsung Tunai (BLT)':
    id = 4
elif nama_program == 'Kartu Indonesia Pintar (KIP)':
    id = 5
elif nama_program == 'Kartu Indonesia Sehat (KIS)':
    id = 6
elif nama_program == 'Bantuan Sosial Beras Sejahtera (Rastra)':
    id = 7
elif nama_program == 'Beras untuk Keluarga Miskin (RASKIN)':
    id = 8
elif nama_program == 'KUBE':
    id = 9
elif nama_program == 'Program Sembako':
    id = 10
elif nama_program == 'Rehabilitasi Sosial':
    id = 11
elif nama_program == 'KAT':
    id = 12

extracted_data = {"id":id,
                  "nama_program": nama_program,
                  "total_positive": len(data.query(f'category == 1.0')),
                  "summary_positive":pos_summary,
                  "total_negative": len(data.query(f'category == 0.0')),
                  "summary_negative":neg_summary,
                  }


extracted_data['last_update'] = datetime.now().strftime("%Y%m%d_%H%M%S")
supabase_client.table('kata_masyarakat').upsert(extracted_data,  returning="minimal", on_conflict="nama_program").execute()