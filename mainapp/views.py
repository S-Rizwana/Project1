from django.shortcuts import render


def main_index(req):
    return render (req,'main/main-index.html')
    
def main_about(req):
    return render (req,'main/main-about.html')

def main_contact(req):
    return render (req,'main/main-contact.html')