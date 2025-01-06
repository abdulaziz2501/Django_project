from django.http import HttpResponse

def my_books(request):
    html = """
        <h1>My Books</h1>
        <ul>
            <li><a href="Istiqlol_jallodlari">Istiqlol Jallodlari</a></li>
            <li><a href="O'tkan_kunlar">O'tkan Kunlar</a></li>
            <li><a href="Mehrobdan_chayon">Mehrobdan Chayon</a></li>
            <li><a href="Qor_qiyg'ir">Qor Qiyg'ir</a></li>
            <li><a href="Olovli_yillar">Olovli Yillar</a></li>
            <li><a href="Ufq">Ufq</a></li>
            <li><a href="Choliqushi">Choliqushi</a></li>
            <li><a href="Shum_bola">Shum Bola</a></li>
            <li><a href="Temur_tuzuklari">Temur Tuzuklari</a></li>
            <li><a href="Sarvqomat_dilbarim">Sarvqomat Dilbarim</a></li>
        </ul>
        <a href="back">Ortga</a>
    """
    return HttpResponse(html)

def Istiqlol_jallodlari(request):
    html = """
        <h1>Istiqlol Jallodlari</h1>
        <p>Abdulla Qodiriy asari bo'lib, milliy istiqlol uchun kurashgan qahramonlar taqdiri haqida hikoya qiladi.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)

def Otkan_kunlar(request):
    html = """
        <h1>O'tkan Kunlar</h1>
        <p>Abdulla Qodiriy tomonidan yozilgan tarixiy-romantik asar.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)

def Mehrobdan_chayon(request):
    html = """
        <h1>Mehrobdan Chayon</h1>
        <p>Abdulla Qahhorning qiziqarli sarguzasht romani.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)

def Qor_qiygir(request):
    html = """
        <h1>Qor Qiyg'ir</h1>
        <p>Abdulla Qahhorning voqealar rivoji bilan boyigan asari.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)

def Olovli_yillar(request):
    html = """
        <h1>Olovli Yillar</h1>
        <p>Sa'dulla Siyoevning ikkinchi jahon urushi davridagi voqealarni aks ettirgan romani.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)

def Ufq(request):
    html = """
        <h1>Ufq</h1>
        <p>Abdulla Qahhorning o‘zbek hayotini tasvirlagan romanlaridan biri.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)

def Choliqushi(request):
    html = """
        <h1>Choliqushi</h1>
        <p>Reshat Nuri Guntekinning romantik va tarixiy romani.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)

def Shum_bola(request):
    html = """
        <h1>Shum Bola</h1>
        <p>G'afur G'ulomning bolalik haqidagi hazilomuz hikoyalari to'plami.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)

def Temur_tuzuklari(request):
    html = """
        <h1>Temur Tuzuklari</h1>
        <p>Amir Temurning o'z hukmronlik qoidalarini bayon etgan asari.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)

def Sarvqomat_dilbarim(request):
    html = """
        <h1>Sarvqomat Dilbarim</h1>
        <p>Pirimqul Qodirovning romantik voqealar asosidagi romanlaridan biri.</p>
        <a href="../">Ortga</a>
    """
    return HttpResponse(html)