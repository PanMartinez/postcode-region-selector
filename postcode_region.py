from django.core.management.base import BaseCommand

import re

from partners.models import Partner, Region


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):

        region_1 = Region.objects.get(id=1) # dolnoslaskie
        region_2 = Region.objects.get(id=2) # kujawsko-pomorskie
        region_3 = Region.objects.get(id=3) # lubelskie
        region_4 = Region.objects.get(id=4) # lubuskie
        region_5 = Region.objects.get(id=5) # lodzkie
        region_6 = Region.objects.get(id=6) # malopolskie
        region_7 = Region.objects.get(id=7) # mazowieckie
        region_8 = Region.objects.get(id=8) # opolskie
        region_9 = Region.objects.get(id=9) # podkarpackie
        region_10 = Region.objects.get(id=10) # podlaskie
        region_11 = Region.objects.get(id=11) # pomorskie
        region_12 = Region.objects.get(id=12) # slaskie
        region_13 = Region.objects.get(id=13) # swietokrzyskie
        region_14 = Region.objects.get(id=14) # warminsko-mazurskie
        region_15 = Region.objects.get(id=15) # wielkopolskie
        region_16 = Region.objects.get(id=16) # Zachodniopomorskie

        partners = Partner.objects.filter(region__isnull=True, country_id=1)

        for partner in partners:

            match = re.search(r'(?P<kod>(?P<prefix>\d{2})-(?P<postcode>\d{3}))', str(partner.address))

            if match:

                prefix = int(match.group('prefix'))
                postcode = int(match.group('postcode'))

                if prefix in range(0, 10):
                    partner.region = region_7
                    partner.save()
                    print(partner.region, region_7)

                elif prefix in range(10, 15):
                    partner.region = region_14
                    partner.save()
                    print(partner.region, region_14)

                elif prefix in range(15, 20):

                    if prefix == 19 and postcode in range(300, 600):
                        partner.region = region_14
                        partner.save()
                        print(partner.region, region_14)
                    else:
                        partner.region = region_10
                        partner.save()
                        print(partner.region, region_10)

                elif prefix in range(20, 25):
                    partner.region = region_3
                    partner.save()
                    print(partner.region, region_3)

                elif prefix == 25:
                    partner.region = region_13
                    partner.save()
                    print(partner.region, region_13)

                elif prefix == 26:

                    if postcode in range(0, 300):
                        partner.region = region_13
                        partner.save()
                        print(partner.region, region_13)

                    elif postcode in range(300, 400):
                        partner.region = region_5
                        partner.save()
                        print(partner.region, region_5)

                    else:
                        partner.region = region_7
                        partner.save()
                        print(partner.region, region_7)

                elif prefix in range(27, 30):

                    if prefix == 27 and postcode == 100:
                        partner.region = region_7
                        partner.save()
                        print(partner.region, region_7)

                    else:
                        partner.region = region_13
                        partner.save()
                        print(partner.region, region_13)

                elif prefix in range(30, 34):
                    partner.region = region_6
                    partner.save()
                    print(partner.region, region_6)

                elif prefix == 34:

                    if postcode in range(300, 400):
                        partner.region = region_12
                        partner.save()
                        print(partner.region, region_12)
                    else:
                        partner.region = region_6
                        partner.save()
                        print(partner.region, region_6)

                elif prefix in range(35, 40):
                    partner.region = region_9
                    partner.save()
                    print(partner.region, region_9)

                elif prefix in range(40, 45):
                    partner.region = region_12
                    partner.save()
                    print(partner.region, region_12)

                elif prefix in range(45, 50):

                    if prefix == 47 and postcode in range(400, 500):
                        partner.region = region_12
                        partner.save()
                        print(partner.region, region_12)
                    else:
                        partner.region = region_8
                        partner.save()
                        print(partner.region, region_8)

                elif prefix in range(50, 60):
                    partner.region = region_1
                    partner.save()
                    print(partner.region, region_1)

                elif prefix in range(60, 65):
                    partner.region = region_15
                    partner.save()
                    print(partner.region, region_15)

                elif prefix in range(65, 70):

                    if prefix == 67 and postcode in range(200, 300):
                        partner.region = region_1
                        partner.save()
                        print(partner.region, region_1)

                    else:
                        partner.region = region_4
                        partner.save()
                        print(partner.region, region_4)

                elif prefix in range(70, 80):

                    if prefix == 76 and postcode in range(200, 40):
                        partner.region = region_11
                        partner.save()
                        print(partner.region, region_11)

                    elif prefix == 77 and postcode in range(100, 400):
                        partner.region = region_11
                        partner.save()
                        print(partner.region, region_11)

                    elif prefix == 77 and postcode in range(400, 500):
                        partner.region = region_15
                        partner.save()
                        print(partner.region, region_15)

                    else:
                        partner.region = region_16
                        partner.save()
                        print(partner.region, region_16)

                elif prefix in range(80, 85):

                    if prefix == 82 and postcode in range(300, 400):
                        partner.region = region_14
                        partner.save()
                        print(partner.region, region_14)

                    else:
                        partner.region = region_11
                        partner.save()
                        print(partner.region, region_11)

                elif prefix in range(85, 90):

                    if prefix == 89 and postcode in range(300, 400):
                        partner.region = region_15
                        partner.save()
                        print(partner.region, region_15)

                    elif prefix == 89 and postcode in range(600, 700):
                        partner.region = region_11
                        partner.save()
                        print(partner.region, region_11)

                    else:
                        partner.region = region_2
                        partner.save()
                        print(partner.region, region_2)

                elif prefix in range(90, 100):

                    if prefix == 96 and postcode in range(300, 600):
                        partner.region = region_7
                        partner.save()
                        print(partner.region, region_7)

                    else:
                        partner.region = region_5
                        partner.save()
                        print(partner.region, region_5)

            else:
                print(partner.id, partner.name)