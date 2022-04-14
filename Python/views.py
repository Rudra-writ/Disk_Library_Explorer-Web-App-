from django.shortcuts import render
from django.conf import settings
import PyPDF2
import glob
import textract
import re
import pandas as pd
import multiprocessing as mp
from pathlib import Path
import webbrowser
import subprocess
import json
import os


def first_page(request):
    if( request.method == 'POST'):
        directory_list = os.listdir("C:/libvirtualenv/LIBRARY")
        if(request.POST.get('search2') and request.POST.get('file')):
            title_df = pd.DataFrame(columns = ['file'])
            matching_files = pd.DataFrame(columns = ['file'])

            master_keywords = request.POST.get('file')
            non_search_words = master_keywords.split('-')[1] if '-' in master_keywords else 'none'
            non_search_words = non_search_words.split('-') if '-' in non_search_words else 'none'
            search_words = master_keywords.split('-')[0] if '-' in master_keywords else master_keywords
            search_words = search_words.split('+')
            paths = []
            paths = glob.glob("C:/libvirtualenv/LIBRARY/**/*.pdf" )

            for files in paths:
                try:

                  
                    file_name = files.split("/")[-1]
                   
    
                    if all(words.casefold() in file_name.casefold() for words in search_words):

                        title_df.at[0,'file'] = files
                        print(file_name)
                        matching_files = matching_files.append(title_df)
                        title_df = title_df[0:0]

                except:
                    continue

            matching_files.reset_index(drop = True, inplace = True)
            matching_files = matching_files.drop_duplicates()
            matching_files['file'] = matching_files.file.replace({'C:/libvirtualenv/LIBRARY':''}, regex= True)
           
            json_records = matching_files.reset_index().to_json(orient = 'records')
            file_names = []
            file_names = json.loads(json_records)

            return render(request,'first_page.html', { 'file_names': file_names, 'directories': directory_list})
        
        elif (request.POST.get('keyword') and request.POST.get('search') and request.POST.get('directory') == ''):
            
             df = pd.DataFrame(columns = ['file', 'page'])
             df2 = pd.DataFrame(columns = ['file', 'page'])
             df3 = pd.DataFrame(columns = ['file', 'page'])
             df4 = pd.DataFrame(columns = ['file', 'page'])


             master_keywords = request.POST.get('keyword')
             non_search_words = master_keywords.split('-')[1] if '-' in master_keywords else 'none'
             non_search_words = non_search_words.split('-') if '-' in master_keywords else 'none'
             search_words = master_keywords.split('-')[0] if '-' in master_keywords else master_keywords
             search_words = search_words.split('+')
             search_words1 = [' {0} '.format(elem) for elem in search_words ]
             search_words2 = [' {0}'.format(elem) for elem in search_words ]
             search_words3 = ['{0} '.format(elem) for elem in search_words ]
             search_words1.extend(search_words2)
             search_words1.extend(search_words3)
           
             paths = []
             paths = glob.glob("C:\libvirtualenv\LIBRARY\**\*.pdf" )

             for files in paths:
                 try:
                     pdfFileObj = open(files, 'rb')
                     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        
 
                     pages = []
                     no_of_pages = int(pdfReader.numPages)
                     search_length = no_of_pages if (int(request.POST.get('pages')) > no_of_pages) else int(request.POST.get('pages'))

                     for num in range( search_length):
                        pageObj = pdfReader.getPage(num)
                        c = 0
                        text = (pageObj.extractText())
                        if all(words.casefold() in text.casefold() for words in search_words) and (not all(words.casefold() in text.casefold() for words in non_search_words) or non_search_words == 'none' ):
                            df.at[0,'file'] = files
                            df.at[0,'page']= num+1
                           
                            df2=df2.append(df)
                            df = df[0:0]
                 except:
                     continue

             df2.reset_index(drop = True, inplace = True)
             df2 = df2.drop_duplicates()
             file_names = df2['file'].unique()
             i = 0
             for file1 in file_names:
                df3=df2.loc[df2['file'] == file1]
                pages = df3['page'].to_list()
                page_list = ','
               
                df4.at[i,'file'] = file1
                df4.at[i,'page'] = pages
                df3 = df3[0:0]
                i = i + 1
             
             json_records2 = df4.reset_index().to_json(orient = 'records')
             recommended_files = []
             recommended_files = json.loads(json_records2)
             
             return render(request,'first_page.html', { 'content': recommended_files, 'directories': directory_list})

        elif (request.POST.get('keyword') and request.POST.get('search') and request.POST.get('directory') != ''):

             df = pd.DataFrame(columns = ['file', 'page'])
             df2 = pd.DataFrame(columns = ['file', 'page'])
             df3 = pd.DataFrame(columns = ['file', 'page'])
             df4 = pd.DataFrame(columns = ['file', 'page'])


             master_keywords = request.POST.get('keyword')
             non_search_words = master_keywords.split('-')[1] if '-' in master_keywords else 'none'
             non_search_words = non_search_words.split('-') if '-' in master_keywords else 'none'
             search_words = master_keywords.split('-')[0] if '-' in master_keywords else master_keywords
             search_words = search_words.split('+')
             search_words1 = [' {0} '.format(elem) for elem in search_words ]
             search_words2 = [' {0}'.format(elem) for elem in search_words ]
             search_words3 = ['{0} '.format(elem) for elem in search_words ]
             search_words1.extend(search_words2)
             search_words1.extend(search_words3)
             print(search_words1)

             directory_name= Path(request.POST.get('directory'))
             root = Path("C:/libvirtualenv/LIBRARY/")
             file_path = Path("C:/libvirtualenv/LIBRARY/*.pdf")
             chld = file_path.relative_to(root)
             file_path1 = root/directory_name/chld
           
             paths = glob.glob(str(file_path1))

             

             for files in paths:
                 try:
                     pdfFileObj = open(files, 'rb')
                     pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  
 
                     pages = []
                     no_of_pages = int(pdfReader.numPages)
                     search_length = no_of_pages if (int(request.POST.get('pages')) > no_of_pages) else int(request.POST.get('pages'))
                     
                     for num in range( search_length):
                        pageObj = pdfReader.getPage(num)
                        c = 0
                        text = (pageObj.extractText())
                        if all(words.casefold() in text.casefold() for words in search_words) and (not all(words.casefold() in text.casefold() for words in non_search_words) or non_search_words == 'none' ):
                        #if re.search( (r'\b'+ word + r'\b' for word in search_words), text) and (non_search_words == 'none'  or not (re.search( (r'\b'+ word + r'\b' for word in non_search_words), text))):
                            df.at[0,'file'] = files
                            df.at[0,'page']= num+1
                           
                            df2=df2.append(df)
                            df = df[0:0]
                 except:
                     continue

             df2.reset_index(drop = True, inplace = True)
             df2 = df2.drop_duplicates()
             file_names = df2['file'].unique()
             i = 0
             for file1 in file_names:
                df3=df2.loc[df2['file'] == file1]
                pages = df3['page'].to_list()
               
                df4.at[i,'file'] = file1
                df4.at[i,'page'] = pages
                df3 = df3[0:0]
                i = i + 1
             df4['file'] = df4.file.replace({'C:/libvirtualenv/LIBRARY': ''}, regex= True)
             json_records2 = df4.reset_index().to_json(orient = 'records')
             recommended_files = []
             recommended_files = json.loads(json_records2)
             
             return render(request,'first_page.html', {'content': recommended_files, 'directories': directory_list})








        else:
            directory_list = os.listdir("C:\libvirtualenv\LIBRARY")
            return render(request,'first_page.html', {'directories': directory_list})




        
    else:
        directory_list = os.listdir("C:\libvirtualenv\LIBRARY")
        return render(request,'first_page.html', {'directories': directory_list})

# Create your views here.
