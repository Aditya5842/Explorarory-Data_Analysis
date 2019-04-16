def links_of_url(url):
    '''Returns the list of downloadable link of ftp including parent directory'''
    import  urllib.request
    import re
    open_url = urllib.request.urlopen(url)
    url_data = open_url.read() #it is in bytes data type
    url_text = url_data.decode('utf-8') #string data type
    c = []
    for i in url_text.split():
        if re.search('href=',i):
            c.append(url+i.split('"')[1])
    return c

def download_file(url):
    '''Dowload the file from given link'''
    import  urllib.request
    c = links_of_url(url)
    for i in range(1,len(c)+1): # to remove parent directory
        urllib.request.urlretrieve(c[i],Name +str(i))

link = input('Give the address: ')
Name = input('Give the File Name:')
print('Files will be downloaed to same folder where this file is')
print('File is downlading:')
download_file(link)
