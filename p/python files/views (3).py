from django.shortcuts import render, render_to_response, RequestContext, redirect
from intra.libs.base import Base
import json
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from datetime import datetime, date
from django.forms import DateField, IntegerField, CharField
from django.db import connection
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def logout(request):

	auth.logout(request)
	return render_to_response('login.html')

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/home')
	else:
		return HttpResponseRedirect('/invalid')

def loggedin(request):
    xbj = Base()

    row = xbj.dictfetchall(sql='select count(*) AS victims from v_victims')
    dm = xbj.dictfetchall(sql='select count(*) AS death from v_death_missing')
    inc = xbj.dictfetchall(sql='select * from v_number_incidents_year WHERE period_year = 2015')
    #mn = xbj.dictfetchall(sql='select count (*) AS month from v_victims where ((extract(year from incident_date) = 2015) or (_incident_yr = 2015)) and (extract(month from incident_date)  in (5))')
    yr = xbj.dictfetchall(sql='select count (*) AS year from v_victims where ((extract(year from incident_date) = 2015) or (_incident_yr = 2015))')

    return render_to_response('index.html',
							 {'deathcount': dm, 'victimscount': row, 'incidents': inc,'byyear': yr, 'full_name': request.user.username})

def invalid_login(request):
	return render_to_response('login.html')




def signin(request):
    return render_to_response("login.html",
				    context_instance=RequestContext(request))

#def login(request):
    #username = request.POST['username']
    #password = request.POST['password']
    #user = authenticate(username=username, password=password)
    #if user is not None:
       # if user.is_active:
           # login(request, user)
            #return redirect ("home")
       # else:
            #return redirect ("signin")
    #else:
        #return redirect ("signin")


def visualsDistrict(request):
    xbj = Base()

    year_range = range(datetime.now().year, 1998, -1)
    row = xbj.dictfetchall(sql="select * FROM t_districts")
    urls = xbj.dictfetchall(sql="select * FROM intra_urls WHERE grp = 'stationary' ")
    vls = xbj.dictfetchall(sql="select * FROM intra_urls WHERE grp = 'visuals' ")


    return render_to_response("visuals_by_district.html", {'menu': urls,'vls':vls,'yearange': year_range, 'minyear': year_range[-1], 'row': row,'full_name': request.user.username }, context_instance=RequestContext(request))

def maps(request):
    xbj = Base()

    row = xbj.dictfetchall(sql="select * FROM intra_stationary")

    return render_to_response("maps.html",{'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))


def statphysio(request):
    xbj = Base()

    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'physio' ")

    return render_to_response("statphysio.html",{'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def statcounselling(request):
    xbj = Base()

    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'counselling' ")

    return render_to_response("statcounselling.html",{'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def statlegal(request):
    xbj = Base()

    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'legal' ")

    return render_to_response("statlegal.html",{'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def statoutreach(request):
    xbj = Base()

    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'outreach' ")

    return render_to_response("statoutreach.html",{'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def statclinic(request):
    xbj = Base()

    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'clinic' ")
    urls = xbj.dictfetchall(sql="select * FROM intra_urls")

    return render_to_response("statclinic.html",{'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def stationery(request):
    xbj = Base()
    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'clinic'")
    urls = xbj.dictfetchall(sql="select * FROM intra_urls")


    return render_to_response("stationary.html",{'menu': urls,'stationery': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def hr(request):
    xbj = Base()
    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'hr'")
    urls = xbj.dictfetchall(sql="select * FROM intra_urls")

    return render_to_response("stathr.html",{'menu': urls,'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def finance(request):
    xbj = Base()
    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'finance'")
    urls = xbj.dictfetchall(sql="select * FROM intra_urls")

    return render_to_response("statfinance.html",{'menu': urls,'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def workshops(request):
    xbj = Base()
    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'workshops'")
    urls = xbj.dictfetchall(sql="select * FROM intra_urls")

    return render_to_response("statworkshop.html",{'menu': urls,'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def admini(request):
    xbj = Base()
    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'admin'")
    urls = xbj.dictfetchall(sql="select * FROM intra_urls")

    return render_to_response("statadmin.html",{'menu': urls,'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))

def conslng(request):
    xbj = Base()
    row = xbj.dictfetchall(sql="select * FROM intra_stationary where department = 'counselling'")
    urls = xbj.dictfetchall(sql="select * FROM intra_urls")

    return render_to_response("statconslg.html",{'menu': urls,'stationary': row, 'full_name': request.user.username},  context_instance=RequestContext(request))



def visuals(request):
    xbj = Base()

    year_range = range(datetime.now().year, 1998, -1)
    urls = xbj.dictfetchall(sql="select * FROM intra_urls WHERE grp = 'stationary' ")
    vls = xbj.dictfetchall(sql="select * FROM intra_urls WHERE grp = 'visuals' ")

    return render_to_response("visuals.html", {'menu': urls,'vls':vls,'yearange': year_range, 'minyear': year_range[-1],'full_name': request.user.username}, context_instance=RequestContext(request))


def home(request):
    xbj = Base()

    row = xbj.dictfetchall(sql='select count(*) AS victims from v_victims')
    dm = xbj.dictfetchall(sql='select count(*) AS death from v_death_missing')
    inc = xbj.dictfetchall(sql='select * from v_number_incidents_year WHERE period_year = 2015')
    #mn = xbj.dictfetchall(sql='select count (*) AS month from v_victims where ((extract(year from incident_date) = 2015) or (_incident_yr = 2015)) and (extract(month from incident_date)  in (5))')
    yr = xbj.dictfetchall(sql='select count (*) AS year from v_victims where ((extract(year from incident_date) = 2015) or (_incident_yr = 2015))')
    urls = xbj.dictfetchall(sql="select * FROM intra_urls WHERE grp = 'stationary' ")
    vls = xbj.dictfetchall(sql="select * FROM intra_urls WHERE grp = 'visuals' ")

    #smevents = __summary_events(request)

    return render_to_response("index.html", {'menu': urls,'vls':vls,'deathcount': dm, 'victimscount': row, 'incidents': inc,'byyear': yr, 'full_name': request.user.username}, context_instance=RequestContext(request))

def counselling(request):
    xbj = Base()

    #row = xbj.dictfetchall(sql="select * FROM t_infographics")

    return render_to_response("counselling.html",{'full_name': request.user.username},  context_instance=RequestContext(request))

def ajax_counselling(request):
    data = {}

    frm = DateField(required=False, input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y'])

    try:

        fdate = frm.clean(request.GET['datetimepicker1'])
        tdate = frm.clean(request.GET['datetimepicker2'])


    except:

        fdate = datetime.now().date()
        tdate = datetime.now().date()

    if not fdate or not tdate :
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    xbj = Base()
    cs = xbj.dictfetchall(sql="select count(*) AS counsel from q_counselling WHERE entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    intl = xbj.dictfetchall(sql="select count(*) AS initial from q_counselling WHERE general_visit_type = 'Initial' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    flp = xbj.dictfetchall(sql="select count(*) AS follow from q_counselling WHERE general_visit_type = 'Follow Up' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    icst = xbj.dictfetchall(sql="select count(*) AS ctype from q_counselling WHERE counsel_session_type = 'Individual' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gcst = xbj.dictfetchall(sql="select count(*) AS gctype from q_counselling WHERE counsel_session_type = 'Group' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrf = xbj.dictfetchall(sql="select count(*) AS genderf from q_counselling WHERE gender = 'F' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrm = xbj.dictfetchall(sql="select count(*) AS genderm from q_counselling WHERE gender = 'M' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))

    data['counsel'] = cs[0]["counsel"] if cs else 0
    data['initial'] = intl[0]["initial"] if intl else 0
    data['follow'] = flp[0]["follow"] if flp else 0
    data['ctype'] = icst[0]["ctype"] if icst else 0
    data['gctype'] = gcst[0]["gctype"] if gcst else 0
    data['genderf'] = gndrf[0]["genderf"] if gcst else 0
    data['genderm'] = gndrm[0]["genderm"] if gcst else 0


    return HttpResponse(json.dumps(data), content_type='application/json')

def clinic(request):
    xbj = Base()

    #row = xbj.dictfetchall(sql="select * FROM t_infographics")

    return render_to_response("clinic.html",{'full_name': request.user.username},  context_instance=RequestContext(request))

def ajax_clinic(request):
    data = {}

    frm = DateField(required=False, input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y'])

    try:
        fdate = frm.clean(request.GET['datetimepicker1'])
        tdate = frm.clean(request.GET['datetimepicker2'])

    except:
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    if not fdate or not tdate :
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    xbj = Base()
    cs = xbj.dictfetchall(sql="select count(*) AS counsel from q_counselling WHERE entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    intl = xbj.dictfetchall(sql="select count(*) AS initial from q_counselling WHERE general_visit_type = 'Initial' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    flp = xbj.dictfetchall(sql="select count(*) AS follow from q_counselling WHERE general_visit_type = 'Follow Up' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    icst = xbj.dictfetchall(sql="select count(*) AS ctype from q_counselling WHERE counsel_session_type = 'Individual' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gcst = xbj.dictfetchall(sql="select count(*) AS gctype from q_counselling WHERE counsel_session_type = 'Group' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrf = xbj.dictfetchall(sql="select count(*) AS genderf from q_counselling WHERE gender = 'F' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrm = xbj.dictfetchall(sql="select count(*) AS genderm from q_counselling WHERE gender = 'M' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))

    data['counsel'] = cs[0]["counsel"] if cs else 0
    data['initial'] = intl[0]["initial"] if intl else 0
    data['follow'] = flp[0]["follow"] if flp else 0
    data['ctype'] = icst[0]["ctype"] if icst else 0
    data['gctype'] = gcst[0]["gctype"] if gcst else 0
    data['genderf'] = gndrf[0]["genderf"] if gcst else 0
    data['genderm'] = gndrm[0]["genderm"] if gcst else 0


    return HttpResponse(json.dumps(data), content_type='application/json')

def physio(request):
    xbj = Base()


    return render_to_response("physio.html",{'full_name': request.user.username},  context_instance=RequestContext(request))

def ajax_physio(request):
    data = {}

    frm = DateField(required=False, input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y'])

    try:
        fdate = frm.clean(request.GET['datetimepicker1'])
        tdate = frm.clean(request.GET['datetimepicker2'])

    except:
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    if not fdate or not tdate :
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    xbj = Base()
    cs = xbj.dictfetchall(sql="select count(*) AS counsel from q_counselling WHERE entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    intl = xbj.dictfetchall(sql="select count(*) AS initial from q_counselling WHERE general_visit_type = 'Initial' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    flp = xbj.dictfetchall(sql="select count(*) AS follow from q_counselling WHERE general_visit_type = 'Follow Up' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    icst = xbj.dictfetchall(sql="select count(*) AS ctype from q_counselling WHERE counsel_session_type = 'Individual' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gcst = xbj.dictfetchall(sql="select count(*) AS gctype from q_counselling WHERE counsel_session_type = 'Group' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrf = xbj.dictfetchall(sql="select count(*) AS genderf from q_counselling WHERE gender = 'F' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrm = xbj.dictfetchall(sql="select count(*) AS genderm from q_counselling WHERE gender = 'M' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))

    data['counsel'] = cs[0]["counsel"] if cs else 0
    data['initial'] = intl[0]["initial"] if intl else 0
    data['follow'] = flp[0]["follow"] if flp else 0
    data['ctype'] = icst[0]["ctype"] if icst else 0
    data['gctype'] = gcst[0]["gctype"] if gcst else 0
    data['genderf'] = gndrf[0]["genderf"] if gcst else 0
    data['genderm'] = gndrm[0]["genderm"] if gcst else 0


    return HttpResponse(json.dumps(data), content_type='application/json')

def outreach(request):
    xbj = Base()


    return render_to_response("outreach.html",{'full_name': request.user.username},  context_instance=RequestContext(request))

def ajax_outreach(request):
    data = {}

    frm = DateField(required=False, input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y'])

    try:
        fdate = frm.clean(request.GET['datetimepicker1'])
        tdate = frm.clean(request.GET['datetimepicker2'])

    except:
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    if not fdate or not tdate :
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    xbj = Base()
    cs = xbj.dictfetchall(sql="select count(*) AS counsel from q_counselling WHERE entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    intl = xbj.dictfetchall(sql="select count(*) AS initial from q_counselling WHERE general_visit_type = 'Initial' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    flp = xbj.dictfetchall(sql="select count(*) AS follow from q_counselling WHERE general_visit_type = 'Follow Up' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    icst = xbj.dictfetchall(sql="select count(*) AS ctype from q_counselling WHERE counsel_session_type = 'Individual' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gcst = xbj.dictfetchall(sql="select count(*) AS gctype from q_counselling WHERE counsel_session_type = 'Group' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrf = xbj.dictfetchall(sql="select count(*) AS genderf from q_counselling WHERE gender = 'F' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrm = xbj.dictfetchall(sql="select count(*) AS genderm from q_counselling WHERE gender = 'M' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))

    data['counsel'] = cs[0]["counsel"] if cs else 0
    data['initial'] = intl[0]["initial"] if intl else 0
    data['follow'] = flp[0]["follow"] if flp else 0
    data['ctype'] = icst[0]["ctype"] if icst else 0
    data['gctype'] = gcst[0]["gctype"] if gcst else 0
    data['genderf'] = gndrf[0]["genderf"] if gcst else 0
    data['genderm'] = gndrm[0]["genderm"] if gcst else 0


    return HttpResponse(json.dumps(data), content_type='application/json')

def legal(request):
    xbj = Base()


    return render_to_response("legal.html",{'full_name': request.user.username},  context_instance=RequestContext(request))

def ajax_legal(request):
    data = {}

    frm = DateField(required=False, input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y'])

    try:
        fdate = frm.clean(request.GET['datetimepicker1'])
        tdate = frm.clean(request.GET['datetimepicker2'])

    except:
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    if not fdate or not tdate :
        fdate = datetime.now().date()
        tdate = datetime.now().date()

    xbj = Base()
    cs = xbj.dictfetchall(sql="select count(*) AS counsel from q_counselling WHERE entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    intl = xbj.dictfetchall(sql="select count(*) AS initial from q_counselling WHERE general_visit_type = 'Initial' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    flp = xbj.dictfetchall(sql="select count(*) AS follow from q_counselling WHERE general_visit_type = 'Follow Up' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    icst = xbj.dictfetchall(sql="select count(*) AS ctype from q_counselling WHERE counsel_session_type = 'Individual' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gcst = xbj.dictfetchall(sql="select count(*) AS gctype from q_counselling WHERE counsel_session_type = 'Group' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrf = xbj.dictfetchall(sql="select count(*) AS genderf from q_counselling WHERE gender = 'F' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))
    gndrm = xbj.dictfetchall(sql="select count(*) AS genderm from q_counselling WHERE gender = 'M' And entry_date Between %s AND %s", prms=tuple([fdate.strftime('%d/%m/%Y'),tdate.strftime('%d/%m/%Y')]))

    data['counsel'] = cs[0]["counsel"] if cs else 0
    data['initial'] = intl[0]["initial"] if intl else 0
    data['follow'] = flp[0]["follow"] if flp else 0
    data['ctype'] = icst[0]["ctype"] if icst else 0
    data['gctype'] = gcst[0]["gctype"] if gcst else 0
    data['genderf'] = gndrf[0]["genderf"] if gcst else 0
    data['genderm'] = gndrm[0]["genderm"] if gcst else 0


    return HttpResponse(json.dumps(data), content_type='application/json')



def ajax_data_home(request):
    data = {}

    frm = DateField(required=False, input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y'])
    #frm = IntegerField(required=False)

    try:
        adate = frm.clean(request.GET['datetimepicker1'])

    except:
        adate = datetime.now().date()

    if not adate :
        adate = datetime.now().date()

    # e.g. pyrgraph = xbj.dictfetchall(sql="select * FROM v_district_ages where gender ilike 'F' and dob between %s and %s", prms=(periodfrom.strptime('%Y-%m-%d'), periodto.strptime('%Y-%m-%d'),)

    xbj = Base()
    ie = xbj.dictfetchall(sql="select count(*) AS no_events from t_incident_events WHERE event_date = %s", prms=tuple([adate.strftime('%Y-%m-%d')]))
    inc = xbj.dictfetchall(sql="select count(*) AS no_incident from t_incidents WHERE incident_date = %s", prms=tuple([adate.strftime('%Y-%m-%d')]))

    data['no_events'] = ie[0]["no_events"] if ie else 0
    data['no_incident'] = inc[0]["no_incident"] if inc else 0
    tmpdct = injury_severity(adate)
    data['injury_severity_1_3'] = tmpdct['injury_severity_1_3']
    data['injury_severity_4_5'] = tmpdct['injury_severity_4_5']
    data['no_hospitalized'] = tmpdct['no_hospitalized']


    return HttpResponse(json.dumps(data), content_type='application/json')


def injury_severity(adate):
    data = {}
    data['injury_severity_1_3'] = 0
    data['injury_severity_4_5'] = 0
    data['no_hospitalized'] = 0

    iseverity123 = ('Slight', 'Moderate', 'Moderate to severe',)
    iseverity45 = ('Severe', 'Life threatening',)

    q = 'select (regexp_split_to_array(ht.type_health_state, %s))[1], count(distinct i.id) from t_accts a'
    q += ' inner join t_entries e on e.acct_id = a.id'
    q += ' inner join t_incidents i on i.root_id = e.root_id'
    q += ' inner join t_incident_details dt on dt.root_id = i.root_id'
    q += ' inner join t_health_state h on h.entry_id = e.id and h.ehealth_state_item = %s'
    q += ' inner join t_type_health_state ht on ht.id = h.type_health_state_id'
    q += ' where i.incident_date = %s'
    q += ' group by (regexp_split_to_array(ht.type_health_state, %s))[1]'
    args = []
    args.append('/')
    args.append('sb-med-assess')
    args.append(adate.strftime('%Y-%m-%d'))
    args.append('/')
    rows = get_rows(sql=q, prms=tuple(args))
    if rows:
        num123 = sum([rw[1] for rw in rows if rw[0] in iseverity123])
        num45 = sum([rw[1] for rw in rows if rw[0] in iseverity45])
        data['injury_severity_1_3'] = format_item(vl=num123)
        data['injury_severity_4_5'] = format_item(vl=num45)

    q = 'select count(distinct i.id)'
    q += ' from t_accts a inner join t_entries e on e.acct_id = a.id'
    q += ' inner join t_incidents i on i.root_id = e.root_id'
    q += ' left join t_general g on g.entry_id = e.id'
    q += ' left join t_hospitalizations h on h.entry_id = e.id'
    q += ' where (i.incident_date = %s) and (g.is_hospitalized or (not h.id is null))'
    row = get_one_row(sql=q, prms=(adate.strftime('%Y-%m-%d'),))
    if row:
        data['no_hospitalized'] = format_item(vl=row[0])

    return data

def sort_dictlist(lst, sortkey, otherword='other'):
    ilst = sorted([dct for dct in lst if not dct[sortkey].lower() == otherword.lower()], key=lambda itm: itm[sortkey])
    for xdct in lst:
        if xdct[sortkey].lower() == otherword.lower(): ilst.append(xdct)

    return ilst


def format_item(vl=None, dtfmt=''):
    v = vl
    if vl:
        if type(vl) == type(datetime.now()):
            v = vl.strftime(dtfmt) if dtfmt else vl.strftime('%d/%m/%Y')
        elif type(vl) == type(date.today()):
            v = vl.strftime(dtfmt) if dtfmt else vl.strftime('%d/%m/%Y')
        elif type(vl) == type(datetime.time(datetime.now())):
            v = vl.strftime(dtfmt) if dtfmt else vl.strftime('%H:%M:%f')
    else:
        if type(vl) == type(True): pass
        else: v = ''

    return v

def ajax_data(request):
    data = {}

    #frm = DateField(required=False, input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y'])
    frm = IntegerField(required=False)

    try:
        yearfrom = frm.clean(request.GET['fromyear'])
        yearto = frm.clean(request.GET['toyear'])
        #periodfrom = frm.clean(request.GET['fromyear'])
        #periodto = frm.clean(request.GET['toyear'])
    except:
        yearfrom = 0
        yearto = 0

    if not yearfrom or not yearto:
        yearfrom = 2000
        yearto = datetime.now().year

    # e.g. pyrgraph = xbj.dictfetchall(sql="select * FROM v_district_ages where gender ilike 'F' and dob between %s and %s", prms=(periodfrom.strptime('%Y-%m-%d'), periodto.strptime('%Y-%m-%d'),)

    xbj = Base()
    ts =  xbj.dictfetchall(sql="select * FROM v_number_incidents_year WHERE period_year BETWEEN %s AND %s ORDER BY period_year ASC", prms=(yearfrom, yearto,))
    grp =  xbj.dictfetchall(sql="select * FROM v_age_grp WHERE year BETWEEN %s AND %s ORDER BY year ASC", prms=(yearfrom, yearto,))
    events =  xbj.dictfetchall(sql="select * FROM v_affected_events WHERE year BETWEEN %s AND %s ORDER BY year ASC", prms=(yearfrom, yearto,))
    pk =  xbj.dictfetchall(sql="select * FROM v_incidents_in_years WHERE incident_year BETWEEN %s AND %s ORDER By incident_year Asc", prms=(yearfrom, yearto,))
    mu =  xbj.dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Murder' AND year BETWEEN %s AND %s", prms=(yearfrom, yearto,))
    to =  xbj.dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Torture' AND year BETWEEN %s AND %s", prms=(yearfrom, yearto,))
    sh =  xbj.dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Sexual Harassment' AND year BETWEEN %s AND %s", prms=(yearfrom, yearto,))
    am =  xbj.dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Attempted Murder' AND year BETWEEN %s AND %s", prms=(yearfrom, yearto,))
    assault =  xbj.dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Assaulted'  AND year BETWEEN %s AND %s", prms=(yearfrom, yearto,))
    ab =  xbj.dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Abduction' AND year BETWEEN %s AND %s", prms=(yearfrom, yearto,))
    pep = xbj.dictfetchall(sql="select * FROM v_num_incident_peps1 WHERE year BETWEEN %s AND %s ORDER BY year Asc", prms=(yearfrom, yearto,))
    inj = xbj.dictfetchall(sql="select * FROM v_injury_severity WHERE year BETWEEN %s AND %s ORDER BY year Asc", prms=(yearfrom, yearto,))
    row = xbj.dictfetchall(sql="select * FROM v_num_gender WHERE year BETWEEN %s AND %s ORDER BY year Asc", prms=(yearfrom, yearto,))

    data['ts'] = ts
    data['grp'] = grp
    data['events'] = events
    data['pk'] = pk
    data['mu'] = mu
    data['to'] = to
    data['sh'] = sh
    data['am'] = am
    data['assault'] = assault
    data['ab'] = ab
    data['pep'] = pep
    data['inj'] = inj
    data['row'] = row

    return HttpResponse(json.dumps(data), content_type='application/json')

def ajax_data_district(request):
    data = {}

    #frm = DateField(required=False, input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y'])
    frm = IntegerField(required=False)
    txt = CharField(required=False)

    try:
        bydistrict = txt.clean(request.GET['bydistrict'])
        yearfrom = frm.clean(request.GET['fromyear'])
        yearto = frm.clean(request.GET['toyear'])

        #periodto = frm.clean(request.GET['toyear'])
    except:
        bydistrict = ''
        yearfrom = 0
        yearto = 0


    if not bydistrict or not yearfrom or not yearto:
        bydistrict = 'Harare'
        yearfrom = 2000
        yearto = datetime.now().year


    # e.g. pyrgraph = xbj.dictfetchall(sql="select * FROM v_district_ages where gender ilike 'F' and dob between %s and %s", prms=(periodfrom.strptime('%Y-%m-%d'), periodto.strptime('%Y-%m-%d'),)

    xbj = Base()
    ts =  xbj.dictfetchall(sql="select * FROM v_number_incidents WHERE district = %s AND period_year BETWEEN %s AND %s ORDER BY period_year ASC", prms=(bydistrict, yearfrom, yearto ))
    grp =  xbj.dictfetchall(sql="select * FROM v_age_grp_dist WHERE district = %s AND year BETWEEN %s AND %s ORDER BY year ASC", prms=(bydistrict, yearfrom, yearto ))
    events =  xbj.dictfetchall(sql="select * FROM v_affected_events_dist WHERE district = %s AND year BETWEEN %s AND %s ORDER BY year ASC", prms=(bydistrict, yearfrom, yearto ))
    pk =  xbj.dictfetchall(sql="select * FROM v_incidents_in_years_dist WHERE district = %s AND incident_year BETWEEN %s AND %s ORDER By incident_year Asc", prms=(bydistrict, yearfrom, yearto ))
    pep = xbj.dictfetchall(sql="select * FROM v_num_incident_peps_dist WHERE district = %s AND year BETWEEN %s AND %s ORDER BY year Asc", prms=(bydistrict, yearfrom, yearto ))
    inj = xbj.dictfetchall(sql="select * FROM v_injury_severity_dist WHERE district = %s AND  year BETWEEN %s AND %s ORDER BY year Asc", prms=(bydistrict, yearfrom, yearto ))
    row = xbj.dictfetchall(sql="select * FROM v_num_gender_dist WHERE district = %s AND year BETWEEN %s AND %s ORDER BY year Asc", prms=(bydistrict, yearfrom, yearto ))

    data['ts'] = ts
    data['grp'] = grp
    data['events'] = events
    data['pk'] = pk
    data['pep'] = pep
    data['inj'] = inj
    data['row'] = row

    return HttpResponse(json.dumps(data), content_type='application/json')

def get_rows(sql='', prms=tuple()):
	rws = list()
	if not sql: return rws

	try:
		csr = connection.cursor()

		if prms: csr.execute(sql, prms)
		else: csr.execute(sql)

		rws = csr.fetchall()
	except: print sys.exc_info()

	return rws

def get_one_row(sql='', prms=tuple()):
    found = tuple()
    if not sql: return found

    try:
        csr = connection.cursor()

        if prms: csr.execute(sql, prms)
        else: csr.execute(sql)

        found = csr.fetchone()
    except: found = tuple()

    return found
