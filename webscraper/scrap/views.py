from django.shortcuts import render
import sqlite3


def index(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    news = cursor.execute("""
            SELECT * FROM contents
        """)
    return render(request, 'scrap/index.html', {'news': news})

def search(request):
    value = request.GET['q']
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    news = cursor.execute(f"""
            SELECT * FROM contents WHERE Headlines LIKE '%{value}%'
        """)
    return render(request, 'scrap/index.html', {'news': news})
    