# Generated by Django 3.2.18 on 2024-02-12 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CFPapp', '0007_auto_20240212_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='A1_CO_02',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 J’évalue la fiabilité d’une source, crédibilité et réputation.'), ('Degre_2', 'Degré 2 Je sélectionne les sources les plus pertinentes au regard de mes missions et de la stratégie de ma structure'), ('Degre_3', 'Degré 3 J’évalue la complétude de ma veille. Pour compléter ma veille j’identifie de nouveaux acteurs.'), ('Degre_4', 'Degré 4 Je conseille les décideurs sur la recherche de prestataires et d’outils performants de veille.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A1_CO_03',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je consulte les outils et les acteurs ressources au regard de mes besoins et de mes missions.'), ('Degre_2', 'Degré 2 Je recherche l’information utile dans le système d’informations.'), ('Degre_3', 'Degré 3 Je contextualise les données recensées en fonction de l’organisation de mon environnement'), ('Degre_4', 'Degré 4 J’analyse la diversité des informations recueillies afin de comprendre les transformations'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A2_CO_01',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Structurer une démarche de diagnostic afin d’étudier rigoureusement des besoins en compétences'), ('Degre_2', 'Degré 2 Je repère les enjeux, attentes et besoins du commanditaire.'), ('Degre_3', 'Degré 3 J’organise ma démarche de diagnostic : identification des acteurs clés, choix des outils d’investigations'), ('Degre_4', 'Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner mes pairs sur la structuration et la démarche de diagnostic'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A2_CO_03',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les différents types de note et je connais la structure d’une note ou d’un document d’analyse.'), ('Degre_2', 'Degré 2 Je repère les éléments de mon diagnostic à intégrer dans une note d’opportunité ou une note d’analyse en vue de partager les résultats.'), ('Degre_3', 'Degré 3 Je produis régulièrement des notes et des documents d’analyse en toute autonomie.'), ('Degre_4', 'Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner des pairs à la production de notes et de documents d’analyse.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A3_C1',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais le positionnement de mon organisation dans l’écosystème de la formation professionnelle'), ('Degre_2', 'Degré 2 Je sais positionner mon organisation dans le cadre réglementaire, législatif et sur le marché de la formation professionnelle.'), ('Degre_3', 'Degré 3 Je m’approprie les analyses existantes (diagnostics, notes d’opportunité, plan de développement, …).'), ('Degre_4', 'Degré 4 Je suis un acteur ressource du réseau en capacité de former mes pairs sur la méthodologie d’analyse de marchés.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A3_C2',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je m’informe des résultats, des diagnostics, des enquêtes réalisés et des analyses produites'), ('Degre_2', ' Degré 2J’identifie les potentiels de développement à court, moyen et long terme à partir du diagnostic précis'), ('Degre_3', 'Degré 3 Je propose des axes de développement concrets (moyens et ressources à mobiliser, points de vigilances).'), ('Degre_4', 'Degré 4 Je capitalise et je mutualise les analyses réalisées pour ma structure, le réseau académique.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A3_C3',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je prends connaissance des comptes-rendus des différentes instances.'), ('Degre_2', 'Degré 2 Je participe aux instances de concertation en apportant des éléments d’analyse à soumettre au collectif.'), ('Degre_3', 'Degré 3 Je contribue à l’ordre du jour des instances de concertation.'), ('Degre_4', 'Degré 4 Dans les instances de concertation à l’interne, je suis consulté sur des orientations précises'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A4_C1',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les décideurs (à partir des organigrammes de l’organisation académique et de ma structure)'), ('Degre_2', 'Degré 2 J’identifie le décideur concerné au regard de la situation requérant un conseil.'), ('Degre_3', 'Degré 3 Je m’empare du besoin de conseil, en caractérisant le périmètre, le degré d’urgence et l’impact'), ('Degre_4', 'Degré 4 J’anticipe des situations qui pourraient être sensibles et impactantes pour le développement de ma structure'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A4_C2',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais des méthodes et des outils d’analyse (grille MOFF, diagramme causes effets, brainstorming, etc.).'), ('Degre_2', 'Degré 2 J’utilise une méthode et les outils d’analyse nécessaires à la bonne compréhension de la situation'), ('Degre_3', 'Degré 3  A partir de mon analyse de la situation ou de la demande, j’envisage les pistes de réponses possibles.'), ('Degre_4', 'Degré 4 Je suis un acteur ressource pour le réseau pour accompagner mes pairs sur les méthodes et les outils d’analys'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A4_C3',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les outils de communication adaptés au conseil '), ('Degre_2', 'Degré 2 Je choisis les outils de communication adaptés aux décideurs.'), ('Degre_3', 'Degré 3 Je propose à l’écrit ou à l’oral un contenu synthétique pour être lu ou entendu par les décideurs.'), ('Degre_4', 'Degré 4 A la demande des décideurs, je rédige et je présente un rapport circonstancié'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A5_C1',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les différentes instances de mon territoire, leurs rôles et leur fonctionnement.'), ('Degre_2', 'Degré 2 Je participe aux échanges, aux réunions et aux groupes de travail du territoire.'), ('Degre_3', 'Degré 3 J’adapte ma posture et mes propos en fonction de mes interlocuteurs et des instances auxquelles je participe'), ('Degre_4', 'Degré 4 Je suis sollicité en qualité d’expert de la formation professionnelle'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A5_C2',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je distingue les 3 voies de formation professionnelle. Je m’informe en interne sur les missions, l’offre et les moyens des structures'), ('Degre_2', 'Degré 2 J’identifie sur mon territoire l’offre de formation en m’aidant de la carte des formations professionnelles de l’éducation nationale'), ('Degre_3', 'Degré 3 J’explique la mission de service public de l’éducation nationale'), ('Degre_4', 'Degré 4 Je suis un acteur ressource pour le réseau en capacité d’analyser et d’harmoniser les pratiques de promotion de l’organisation de la formation professionnelle à l’éducation nationale.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A5_C3',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les acteurs socio-économiques de mon territoire. '), ('Degre_2', 'Degré 2 Je construis un réseau de partenaires socio-économiques actualisé et mobilisable'), ('Degre_3', 'Degré 3 Je suis un interlocuteur reconnu et sollicité par les acteurs socio-économiques sur un territoire.'), ('Degre_4', 'Degré 4 Je suis à l’initiative de rencontres partenariales sur un projet donné.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A6_C1',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je connais les éléments constitutifs d’une politique commerciale d’une organisation.'), ('Degre_2', 'Degré 2 J’apporte des éléments d’analyse permettant l’évolution de la politique commerciale au sein d’un collectif'), ('Degre_3', 'Degré 3 Je contribue à la définition des objectifs de la politique commerciale,'), ('Degre_4', 'Degré 4 Je suis un acteur ressource pour le réseau en capacité d’accompagner les équipes en place et transmettre une méthodologie d’élaboration de la politique commerciale.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='A6_C2',
            field=models.CharField(choices=[('Degre_1', 'Degré 1 Je m’informe sur les compétences et les métiers d’avenir et les grands projets de mon territoire,'), ('Degre_2', 'Degré 2 Je rédige un compte-rendu d’entretien et de détection des besoins chez les prospects.'), ('Degre_3', 'Degré 3 Je maitrise les techniques de questionnement et d’écoute active pour réaliser une phase de découverte pertinente.'), ('Degre_4', 'Degré 4 Je partage la méthodologie d’identification des opportunités repérées à l’échelle de mon territoire, de la région académique.'), ('N_S_P', 'Ne se prononce pas')], default='Degre_1', max_length=20),
        ),
    ]
