from api import db, app
from api.models import ApplicationAdNetworkModel, ApplicationModel, AdNetworkModel

def populate_sample():
    try:
        applications = [app for app in ApplicationModel.find_all()]

        if len(applications) < 1:
            app01 = ApplicationModel(**{'name': 'Application 01', 'code': 'APP01'}).save()
            app02 = ApplicationModel(**{'name': 'Application 02', 'code': 'APP02'}).save()
            app03 = ApplicationModel(**{'name': 'Application 03', 'code': 'APP03'}).save()
            app04 = ApplicationModel(**{'name': 'Application 04', 'code': 'APP04'}).save()

            adn01 = AdNetworkModel(**{'name': 'AdNetwork 01', 'code': 'ADN01', 'endpoint': 'http://adn01.com/ads'}).save()
            adn02 = AdNetworkModel(**{'name': 'AdNetwork 02', 'code': 'ADN02', 'endpoint': 'http://adn02.com/ads'}).save()
            adn03 = AdNetworkModel(**{'name': 'AdNetwork 03', 'code': 'ADN03', 'endpoint': 'http://adn03.com/ads'}).save()
            adn04 = AdNetworkModel(**{'name': 'AdNetwork 04', 'code': 'ADN04', 'endpoint': 'http://adn04.com/ads'}).save()

            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn01
            app_adn.score = 1.3
            app01.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn02
            app_adn.score = 2.5
            app01.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn03
            app_adn.score = 3.6
            app01.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn04
            app_adn.score = 4.9
            app01.application_adnetwork.append(app_adn)
            db.session.commit()

            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn01
            app_adn.score = 2.4
            app02.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn02
            app_adn.score = 3.9
            app02.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn03
            app_adn.score = 0.3
            app02.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn04
            app_adn.score = 5.5
            app02.application_adnetwork.append(app_adn)
            db.session.commit()

            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn01
            app_adn.score = 5.2
            app03.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn02
            app_adn.score = 4.1
            app03.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn03
            app_adn.score = 2.0
            app03.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn04
            app_adn.score = 0.9
            app03.application_adnetwork.append(app_adn)
            db.session.commit()

            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn01
            app_adn.score = 0.7
            app04.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn02
            app_adn.score = 1.0
            app04.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn03
            app_adn.score = 6.1
            app04.application_adnetwork.append(app_adn)
            app_adn = ApplicationAdNetworkModel()
            app_adn.ad_network = adn04
            app_adn.score = 3.5
            app04.application_adnetwork.append(app_adn)
            db.session.commit()
        else:
            app.logger.info('Already populated...')
    except Exception as e:
        app.logger.error('Could not populate with sample data: {e}'.format(e=e))
