def visuals(request):
    xbj = Base()


    pyrgraph = xbj.dictfetchall(sql="select * FROM v_district_ages where gender ilike 'F' ")
    pyrmalegraph = xbj.dictfetchall(sql="select * FROM v_district_ages where gender ilike 'M' ")
    dictfemalegraph = xbj.dictfetchall(sql="select * FROM v_district_ages_total where gender ilike 'F' ")
    dictmalegraph = xbj.dictfetchall(sql="select * FROM v_district_ages_total where gender ilike 'M' ")
    ts = xbj.dictfetchall(sql="select * FROM v_number_incidents_year WHERE period_year BETWEEN 2005 AND 2015  ORDER BY period_year Asc")
    grp = xbj.dictfetchall(sql="select * FROM v_age_grp ORDER BY year ASC")
    events = xbj.dictfetchall(sql="select * FROM v_affected_events ORDER BY year Asc")
    ev_pep = xbj.dictfetchall(sql="select * FROM v_affected_events ORDER BY year Asc")
    pep = xbj.dictfetchall(sql="select * FROM v_num_incident_peps1 ORDER BY year Asc")
    inj = xbj.dictfetchall(sql="select * FROM v_injury_severity WHERE year BETWEEN 2005 AND 2015 ORDER BY year Asc")
    pk = xbj.dictfetchall(sql="select * FROM v_incidents_in_years WHERE incident_year BETWEEN 2000 AND 2015")
    row = xbj.dictfetchall(sql="select * FROM v_num_gender WHERE year BETWEEN 2005 AND 2015 ORDER BY year Asc")
    spidergraph = xbj.dictfetchall(sql='select * FROM v_number_incidents_spider Order BY no_incidents Desc limit 8')

    context = {
        'spidergraph': spidergraph,
        'row':row, 'inj': inj, 
        'pep':pep, 'ev_pep':ev_pep, 
        'pk':pk, 
        'events': events, 
        'grp': grp, 
        'pyrgraph': pyrgraph,
        'pyrmalegraph': pyrmalegraph, 
        'dictfemalegraph':dictfemalegraph, 
        'dictmalegraph': dictmalegraph, 
        'ts': ts, 
        }
    template = 'visuals.html'

    return render(template, context , context_instance=RequestContext(request))

