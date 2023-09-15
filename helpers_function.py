import os
import shutil
import requests
from bs4 import BeautifulSoup
import langchain
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter #using text splitter to split the documents into chunks
from langchain.embeddings import OpenAIEmbeddings  # importing the embeddings
from langchain.vectorstores import Chroma # importing chroma db for vector stores
from langchain.chat_models import ChatOpenAI # loading the llm model
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA


api_key = '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'

data = [
    {
        'company_name': 'Woebot Health',
        'url': 'http://www.woebothealth.com/',
        'segment': 'Mental Health'
    },
    {
        'company_name': 'NeuroFlow',
        'url': 'http://www.neuroflow.com/',
        'segment': 'Mental Health'
    },
    {
        'company_name': 'Sonnest Health',
        'url': 'http://www.sonnest.com/',
        'segment': 'Medical Imaging/Cardiovascular'
    }
]

def get_data():
    urls = [d['url'] for d in data]
    company_names = [d['company_name'] for d in data]
    segments = [d['segment'] for d in data]

    return urls, company_names, segments

def get_links(url):
    a_links = []
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    title = soup.title.string.strip()
    print(title)
    links = soup.find_all('a')
    for link in links:
        if link.get('href') == None:
            continue
        if link.get('href').startswith('http'):
            a_links.append(link.get('href'))
    return a_links, title
    
def get_para(link):
    paragraphs = []
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    paras = soup.find_all('p')
    for para in paras:
        paragraphs.append(para.text.strip())

    return paragraphs

def get_text(path):
    with open(path, 'r') as f:
        text = f.read()
    return text

def write_para():
    if os.path.exists('data'):
        shutil.rmtree('data')

    os.mkdir('data')

    path = os.listdir('text/')
    para = ""

    for p in path:
        path = 'text/' + p

        with open(path, 'r') as f:
            text = f.read()
            para = para + '\n' +str(text)
            f.close()

    f = open("data/para.txt", "w")
    f.write(para)
    f.close()

# fuction to load the documents
def load_documents(directory):
    loader = DirectoryLoader(directory)
    documents = loader.load()

    return documents

#fuction to split the documents
def split_documents(documents, chunk_size=1000, chunk_overlap=20):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_documents(documents)

    return chunks

# function to merge scraped text data from the web
def merge_data(company_names):
    path = 'Langchain'
    if os.path.exists(path):
        shutil.rmtree(path)

    os.mkdir('Langchain/')
    os.mkdir('Langchain/data/')

    for company in company_names:
        company_path = company + '/'
        # path = 'langchain_answers'
        para_dir = 'Langchain/data/'+ company_path + 'para.txt'
        os.mkdir('Langchain/data/'+ company_path)

        path = os.listdir('raw_text/' + company_path)
        para = ""

        # extracting the text from txt files and merging them into one file
        for p in path:
            path = 'raw_text/' + company_path + p

            with open(path, 'r') as f:
                text = f.read()
                para = para + '\n' +str(text)
                f.close()

        f = open(para_dir, "w")
        f.write(para)
        f.close()

def llm_ans(docs, questions):

    os.environ['OPENAI_API_KEY'] = api_key
    embeddings = OpenAIEmbeddings()

    model_name = "gpt-3.5-turbo"
    llm = ChatOpenAI(model_name=model_name)

    db = Chroma.from_documents(docs, embeddings)
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm, retriever=retriever, chain_type='stuff')

    # chain = load_qa_chain(llm, chain_type='stuff', verbose=True)

    query = f"Based on the given context, answers all the questions given {questions} in bullet format."
    # matching_docs = db.similarity_search(query)
    # answer = chain.run(input_documents=matching_docs, question=query)
    answer = qa.run(query)

    return answer