from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from intra.views import counselling,ajax_counselling, clinic,ajax_clinic,outreach,ajax_outreach,legal,ajax_legal, physio,ajax_physio,\
        visuals, home, maps,ajax_data, visualsDistrict, ajax_data_district,ajax_data_home, signin, login, logout, \
        loggedin, auth_view, invalid_login,statphysio,statclinic, statcounselling, statlegal, statoutreach, stationery, \
        hr, finance, workshops, admini, conslng

urlpatterns = [
    # Examples:
    url(r'^home/', home, name='home'),
    url(r'^stationery/', stationery, name='stationery'),
    url(r'^stat-physio/', statphysio, name='stat-physio'),
    url(r'^stat-clinic/', statclinic, name='stat-clinic'),
    url(r'^stat-counselling/', statcounselling, name='stat-counselling'),
    url(r'^stat-legal/', statlegal, name='stat-legal'),
    url(r'^statoutreach/', statoutreach, name='stat-outreach'),
    url(r'^stat-hr/', hr, name='stat-hr'),
    url(r'^stat-finance/', finance, name='stat-finance'),
    url(r'^stat-conslng/', conslng, name='stat-conslng'),
    url(r'^stat-workshop/', workshops, name='stat-workshop'),
    url(r'^stat-admin/', admini, name='stat-admin'),
    url(r'^ajax-counselling/', ajax_counselling, name='ajax-counselling'),
    url(r'^counselling/', counselling, name='counselling'),
    url(r'^ajax-clinic/', ajax_clinic, name='ajax-clinic'),
    url(r'^clinic/', clinic, name='clinic'),
    url(r'^ajax-physio/', ajax_physio, name='ajax-physio'),
    url(r'^physio/', physio, name='physio'),
    url(r'^ajax-outreach/', ajax_outreach, name='ajax-outreach'),
    url(r'^outreach/', outreach, name='outreach'),
    url(r'^ajax-legal/', ajax_legal, name='ajax-legal'),
    url(r'^legal/', legal, name='legal'),
    url(r'^$', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^ajax-data-home/', ajax_data_home, name='ajax-data-home'),
    url(r'^signin/', signin, name='signin'),
    url(r'^visuals/', visuals, name='visuals'),
    url(r'^maps/', maps, name='maps'),
    url(r'^ajax-visuals/', ajax_data, name='ajax-visuals'),
    url(r'^ajax-district-visuals/', ajax_data_district, name='ajax-district-visuals'),
    url(r'^visuals-district/', visualsDistrict, name='visuals-district'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^loggedin/', loggedin, name='loggedin'),
    url(r'^invalid/', invalid_login, name='invalid'),
    url(r'^auth/', auth_view, name='auth'),


    url(r'^admin/', include(admin.site.urls)),

]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,
			document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,
			document_root=settings.MEDIA_ROOT)