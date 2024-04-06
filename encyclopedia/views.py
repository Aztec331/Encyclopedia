from django.shortcuts import render
from django.http import HttpResponse
import markdown
from . import util
import random
#1) util.list_entries() gets all the entries 
#2) util.get_entry(titlename) gets all the entries

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        # util.py file's function- list_entries()
    })

#converts markdown files into html
def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def entry(request,title):
    '''Displays the requested entry page, if it exists'''
    #this means if we don't get any HTML file return the error page
    #context dictionaries are important as they display data dyanmically
    #if i have the same layout of the page but different data logically 
    #of different page we should use context dictionaries
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html",{
            "message": "This entry does not exist"
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content
        })

def search(request):
    '''searching the page by fullname and substring'''

    if request.method=="POST":
        entry_search = request.POST['q'] # this means if i searched CSS in the search bar entry_search variable has has the value CSS in it
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html",{
            "title": entry_search,
            "content": html_content
        })
        else:
            allEntries = util.list_entries()
            substringresults= []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    substringresults.append(entry)
            return render(request,"encyclopedia/search.html",{
                "substringresults": substringresults             
            })


def newpage(request):
    '''creating a new page , providing title and '''

    #POST
    if request.method== "POST":
        title = request.POST['title']
        content = request.POST['content'] 
        titleExist = util.get_entry(title)
        #None hai to save karna hai , none nahi to error.html show karna hai
        if titleExist is None:
            util.save_entry(title,content)
            html_content= convert_md_to_html(title)
            return render(request,"encyclopedia/entry.html",{
                "title":title,
                "content":html_content
            })
        else:
            return render(request,"encyclopedia/error.html",{
                "message":"Entry already exists!"
            })
    #GET
    else:
        return render(request, "encyclopedia/newpage.html")


def editpage(request):
    ''' editing the entry page that you're currently on '''
    if request.method=="POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request,"encyclopedia/editpage.html",{
            "title":title,
            "content":content
        })
        
def save_edit(request):
    '''saving the edit of the edit page , save_entry function replaces the previous title with the edited information that you've given on edit page'''
    '''simply put your new info will become the new page and the previous one with the same title will get deleted and replaced by the edited one'''
    if request.method == "POST":
        title= request.POST['title']
        content = request.POST['content']
        util.save_entry(title,content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html",{
            "title": html_content,
            "content": html_content
        })

#don't forget to convert markdown to html
def randumb(request):
    ''' for displaying random pages '''
    all_entries= util.list_entries()
    random_choice = random.choice(all_entries)
    html_content= convert_md_to_html(random_choice)
    return render(request,"encyclopedia/entry.html",{
        "title":random_choice,
        "content": html_content
        })





    
  
    
       




        
        
        


