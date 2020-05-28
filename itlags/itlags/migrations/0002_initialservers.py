# Generated by Django 3.0.6 on 2020-05-28 19:55

from django.db import migrations


class Migration(migrations.Migration):

    def add_initial_servers(apps, schema_editor):
        Server = apps.get_model('itlags', 'Server')
        ServerGroup = apps.get_model('itlags', 'ServerGroup')

        linode = ServerGroup(name = 'Linode')
        linode.save()

        newark = Server(name = 'Newark', url = 'http://speedtest.newark.linode.com/', group=linode)
        newark.save()

        frankfurt = Server(name = 'Frankfurt', url = 'http://speedtest.frankfurt.linode.com/', group=linode)
        frankfurt.save()

        singapore = Server(name = 'Singapore', url = 'http://speedtest.singapore.linode.com/', group=linode)
        singapore.save()

        vultr = ServerGroup(name = 'Vultr')
        vultr.save()

        miami = Server(name = 'Miami', url = 'http://fl-us-ping.vultr.com/', group=vultr)
        miami.save()

        fra = Server(name = 'Frankfurt', url = 'http://fra-de-ping.vultr.com/', group=vultr)
        fra.save()

        sydney = Server(name = 'Sydney', url = 'http://syd-au-ping.vultr.com/', group=vultr)
        sydney.save()


    dependencies = [
        ('itlags', '0001_initial'),
    ]


    operations = [
        migrations.RunPython(add_initial_servers),
    ]
