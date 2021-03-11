from django.urls import path
from django.conf.urls import url 
from .views import * 
# from . views import home,homeo,homeo1,homeo2,homeo3,homeo4,medical,helth,orthotic,dairyfarm,transport,ophthalmology
# from . views import assistantsurgeon,liftescalator,pumpoperator,optometristgr,pulmonary,aa

app_name= 'HelpPsc'
 
urlpatterns = [
    path('',aa , name='aa'),
    path('bb/',bb , name='bb'),
    path('moketest/',test, name='test'),
    path('result/',result, name='result'),

    # path('CraneDriver/',views.homeo , name='homeo'),
    # path('theater_technician/',views.homeo1 , name='homeo1'),
    # path('interior_decoration/',views.homeo2 , name='homeo2'),
    # path('homeopathy/',views.homeo3 , name='homeo3'),
    # path('shift_supervisor/',views.homeo4 , name='homeo4'),
    # path('medical_education/',views.medical , name='medical'),
    # path('helth_services/',views.helth , name='helth'),
    # path('orthotic_engineer/',views.orthotic , name='orthotic'),
    # path('dairy_farm/',views.dairyfarm , name='dairyfarm'),
    # path('motor_transport/',views.transport , name='transport'),
    # path('ophthalmology/',views.ophthalmology , name='ophthalmology'),
    # path('assistant_surgeon/',views.assistantsurgeon , name='assistantsurgeon'),
    # path('lift_escalator/',views.liftescalator , name='liftescalator'),
    # path('pump_operator/',views.pumpoperator , name='pumpoperator'),
    # path('optometrist_gr/',views.optometristgr , name='optometristgr'), 
    # path('pulmonary_medicine/',views.pulmonary , name='pulmonary'),
]
