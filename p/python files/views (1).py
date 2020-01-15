from django.shortcuts import render, render_to_response, RequestContext
from intra.libs.base import Base
import json
from django.http import HttpResponse
from datetime import datetime
from django.forms import DateField

# Create your views here.


def dash(request):
    return render_to_response("index.html",
				   locals(), context_instance=RequestContext(request))

def visuals(request):
    pyrgraph = dictfetchall(sql="select * FROM v_district_ages where gender ilike 'F' ")
    pyrmalegraph = dictfetchall(sql="select * FROM v_district_ages where gender ilike 'M' ")
    dictfemalegraph = dictfetchall(sql="select * FROM v_district_ages_total where gender ilike 'F' ")
    dictmalegraph = dictfetchall(sql="select * FROM v_district_ages_total where gender ilike 'M' ")
    ts = dictfetchall(sql="select * FROM v_number_incidents_time_series ORDER BY period_year")
    grp = dictfetchall(sql="select * FROM v_age_grp ORDER BY year DESC")
    events = dictfetchall(sql="select * FROM v_affected_events")
    pk = dictfetchall(sql="select * FROM v_incidents_in_years WHERE incident_year BETWEEN 2000 AND 2015")
    mu = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Murder' ")
    to = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Torture'")
    sh = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Sexual Harassment' ")
    am = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Attempted Murder' ")
    assault = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Assaulted' ")
    ab = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Abduction'")

    return render_to_response("visuals.html", {'pk':pk, 'ab': ab, 'assault': assault,'am': am,'sh': sh,'to': to, 'mu':mu, 'events': events, 'grp': grp, 'pyrgraph': pyrgraph,'pyrmalegraph': pyrmalegraph, 'dictfemalegraph':dictfemalegraph, 'dictmalegraph': dictmalegraph, 'ts': ts, }, context_instance=RequestContext(request))

def home(request):
    xbj = Base()

    row = dictfetchall(sql='select count(*) AS victims from v_victims')
    dm = dictfetchall(sql='select count(*) AS death from v_death_missing')
    mn = dictfetchall(sql='select count (*) AS month from v_victims where ((extract(year from incident_date) = 2015) or (_incident_yr = 2015)) and (extract(month from incident_date)  in (5))')
    yr = dictfetchall(sql='select count (*) AS year from v_victims where ((extract(year from incident_date) = 2015) or (_incident_yr = 2015))')

    linegraph = xbj.dictfetchall(sql='select * FROM v_district_incidents')
    spidergraph = xbj.dictfetchall(sql='select * FROM v_number_incidents_spider Order BY no_incidents Desc limit 8')
    stackedgraph = xbj.dictfetchall(sql='select * FROM v_district_events')



    return render_to_response("index.html", {'deathcount': dm, 'victimscount': row, 'bymonth': mn,'byyear': yr,'linegraph': linegraph,'spidergraph': spidergraph, 'stackedgraph': stackedgraph }, context_instance=RequestContext(request))

def ajax_data(request):
    data = {}

    frm = DateField(required=False, input_formats=['%d/%m/%Y', '%d-%m-%Y', '%d/%m/%y', '%d-%m-%y'])
    periodfrom = datetime.strptime('01/01/{0}'.format(datetime.now(),), '%d/%m/%Y').date()
    periodto = datetime.now().date()

    try:
        periodfrom = frm.clean(request.POST['fromdate'])
        periodto = frm.clean(request.POST['toate'])
    except:
        periodfrom = datetime.strptime('01/01/{0}'.format(datetime.now(),), '%d/%m/%Y').date()
        periodto = datetime.now().date()

    # e.g. pyrgraph = xbj.dictfetchall(sql="select * FROM v_district_ages where gender ilike 'F' and dob between %s and %s", prms=(periodfrom.strptime('%Y-%m-%d'), periodfrom.strptime('%Y-%m-%d'),)

    pyrgraph = dictfetchall(sql="select * FROM v_district_ages where gender ilike 'F' ")
    pyrmalegraph = dictfetchall(sql="select * FROM v_district_ages where gender ilike 'M' ")
    dictfemalegraph = dictfetchall(sql="select * FROM v_district_ages_total where gender ilike 'F' ")
    dictmalegraph = dictfetchall(sql="select * FROM v_district_ages_total where gender ilike 'M' ")
    ts = dictfetchall(sql="select * FROM v_number_incidents_time_series ORDER BY period_year")
    grp = dictfetchall(sql="select * FROM v_age_grp ORDER BY year DESC")
    events = dictfetchall(sql="select * FROM v_affected_events")
    pk = dictfetchall(sql="select * FROM v_incidents_in_years WHERE incident_year BETWEEN 2000 AND 2015")
    mu = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Murder' ")
    to = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Torture'")
    sh = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Sexual Harassment' ")
    am = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Attempted Murder' ")
    assault = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Assaulted' ")
    ab = dictfetchall(sql="select * FROM v_affected_by_primary_key WHERE incident = 'Abduction'")

    data['pyrgraph'] = pyrgraph
    data['pyrmalegraph'] = pyrmalegraph
    data['dictfemalegraph'] = dictfemalegraph
    data['dictmalegraph'] = dictmalegraph
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
    
    return HttpResponse(json.dumps(data), content_type='application/json')

def dictfetchall(sql='', prms=()):
    rws = {}
    if not sql: return rws

    try:
        csr = connection.cursor()

        if prms: csr.execute(sql, prms)
        else: csr.execute(sql)

        desc = csr.description
        rws = [dict(zip([col[0] for col in desc], rw)) for rw in csr.fetchall()]
    except: rws = {}

    return rws