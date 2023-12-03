# Generated by Django 4.2.6 on 2023-11-30 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0058_alter_recipe_origin_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='origin_country',
            field=models.CharField(choices=[('afghan', 'Afghan'), ('albanian', 'Albanian '), ('algerian', 'Algerian'), ('american', 'American'), ('andorran', 'Andorran'), ('angolan', 'Angolan'), ('argentine', 'Argentine'), ('armenian', 'Armenian'), ('australian', 'Australian'), ('austrian', 'Austrian'), ('azerbaijani', 'Azerbaijani'), ('bahamian', 'Bahamian'), ('bahraini', 'Bahraini'), ('bangladeshi', 'Bangladeshi'), ('barbadian', 'Barbadian'), ('belarusian', 'Belarusian'), ('belgian', 'Belgian'), ('belizean', 'Belizean'), ('beninese', 'Beninese'), ('bhutanese', 'Bhutanese'), ('bolivian', 'Bolivian'), ('bosnian', 'Bosnian'), ('botswanan', 'Botswanan'), ('brazilian', 'Brazilian'), ('british', 'British'), ('bruneian', 'Bruneian'), ('bulgarian', 'Bulgarian'), ('burkinabe', 'Burkinabe'), ('burmese', 'Burmese'), ('burundian', 'Burundian'), ('cambodian', 'Cambodian'), ('cameroonian', 'Cameroonian'), ('canadian', 'Canadian'), ('cape verdean', 'Cape Verdean'), ('central african', 'Central African'), ('chadian', 'Chadian'), ('chilean', 'Chilean'), ('chinese', 'Chinese'), ('colombian', 'Colombian'), ('comoran', 'Comoran'), ('congolese', 'Congolese'), ('costa rican', 'Costa Rican'), ('croatian', 'Croatian'), ('cuban', 'Cuban'), ('cyprio', 'Cyprio'), ('czech', 'Czech'), ('danish', 'Danish'), ('djiboutian', 'Djiboutian'), ('dominican', 'Dominican'), ('dominican republic', 'Dominican Rep.'), ('dutch', 'Dutch'), ('east timorese', 'East Timorese'), ('ecuadorian', 'Ecuadorian'), ('egyptian', 'Egyptian'), ('emirati', 'Emirati'), ('equ. guinean', 'Equ. Guinean'), ('eritrean', 'Eritrean'), ('estonian', 'Estonian'), ('ethiopian', 'Ethiopian'), ('fijian', 'Fijian'), ('filipino', 'Filipino'), ('finnish', 'Finnish'), ('french', 'French'), ('gabonese', 'Gabonese'), ('gambian', 'Gambian'), ('georgian', 'Georgian'), ('german', 'German'), ('ghanaian', 'Ghanaian'), ('greek', 'Greek'), ('grenadian', 'Grenadian'), ('guatemalan', 'Guatemalan'), ('guinean', 'Guinean'), ('guinea-bi.', 'Guinea-Bi.'), ('guyanese', 'Guyanese'), ('haitian', 'Haitian'), ('honduran', 'Honduran'), ('hungarian', 'Hungarian'), ('icelandic', 'Icelandic'), ('indian', 'Indian'), ('indonesian', 'Indonesian'), ('iranian', 'Iranian'), ('iraqi', 'Iraqi'), ('irish', 'Irish'), ('israeli', 'Israeli'), ('italian', 'Italian'), ('ivorian', 'Ivorian'), ('jamaican', 'Jamaican'), ('japanese', 'Japanese'), ('jordanian', 'Jordanian'), ('kazakhstani', 'Kazakhstani'), ('kenyan', 'Kenyan'), ('kiribatian', 'Kiribatian'), ('kuwaiti', 'Kuwaiti'), ('kyrgyz', 'Kyrgyz'), ('laotian', 'Laotian'), ('latvian', 'Latvian'), ('lebanese', 'Lebanese'), ('lesotho', 'Lesotho'), ('liberian', 'Liberian'), ('libyan', 'Libyan'), ('liechtensteiner', 'Liechtensteiner'), ('lithuanian', 'Lithuanian'), ('luxembourgish', 'Luxembourgish'), ('macedonian', 'Macedonian'), ('malagasy', 'Malagasy'), ('malawian', 'Malawian'), ('malaysian', 'Malaysian'), ('maldivian', 'Maldivian'), ('malian', 'Malian'), ('maltese', 'Maltese'), ('marshallese', 'Marshallese'), ('mauritanian', 'Mauritanian'), ('mauritian', 'Mauritian'), ('mexican', 'Mexican'), ('micronesian', 'Micronesian'), ('moldovan', 'Moldovan'), ('monegasque', 'Monegasque'), ('mongolian', 'Mongolian'), ('montenegrin', 'Montenegrin'), ('moroccan', 'Moroccan'), ('mozambican', 'Mozambican'), ('namibian', 'Namibian'), ('nauruan', 'Nauruan'), ('nepalese', 'Nepalese'), ('new zealand', 'New Zealand'), ('nicaraguan', 'Nicaraguan'), ('niger', 'Niger'), ('nigerian', 'Nigerian'), ('north korean', 'North Korean'), ('norwegian', 'Norwegian'), ('omani', 'Omani'), ('pakistani', 'Pakistani'), ('palauan', 'Palauan'), ('palestinian', 'Palestinian'), ('panamanian', 'Panamanian'), ('papua new guinean', 'Papua New Gui.'), ('paraguayan', 'Paraguayan'), ('peruvian', 'Peruvian'), ('polish', 'Polish'), ('portuguese', 'Portuguese'), ('qatari', 'Qatari'), ('romanian', 'Romanian'), ('russian', 'Russian'), ('rwandan', 'Rwandan'), ('saint kitts and nevis', 'St Kitts & Nevis'), ('saint lucian', 'Saint Lucian'), ('saint vincent and the grenadines', 'St Vincent & Grenadines'), ('salvadoran', 'Salvadoran'), ('sammarinese', 'Sammarinese'), ('samoan', 'Samoan'), ('sao tomean', 'Sao Tomean'), ('saudi arabian', 'Saudi Arabian'), ('senegalese', 'Senegalese'), ('serbian', 'Serbian'), ('seychellois', 'Seychellois'), ('sierra leonean', 'Sierra Leonean'), ('singaporean', 'Singaporean'), ('slovak', 'Slovak'), ('slovenian', 'Slovenian'), ('solomon islands', 'Solomon Islands'), ('somali', 'Somali'), ('south african', 'South African'), ('south korean', 'South Korean'), ('south sudanese', 'South Sudanese'), ('spanish', 'Spanish'), ('sri lankan', 'Sri Lankan'), ('sudanese', 'Sudanese'), ('surinamese', 'Surinamese'), ('swazi', 'Swazi'), ('swedish', 'Swedish'), ('swiss', 'Swiss'), ('syrian', 'Syrian'), ('taiwanese', 'Taiwanese'), ('tajik', 'Tajik'), ('tanzanian', 'Tanzanian'), ('thai', 'Thai'), ('togolese', 'Togolese'), ('tongan', 'Tongan'), ('trinidadian and tobagonian', 'Trinidadian & Tobagonian'), ('tunisian', 'Tunisian'), ('turkish', 'Turkish'), ('turkmen', 'Turkmen'), ('tuvaluan', 'Tuvaluan'), ('ugandan', 'Ugandan'), ('ukrainian', 'Ukrainian'), ('uruguayan', 'Uruguayan'), ('uzbek', 'Uzbek'), ('vanuatuan', 'Vanuatuan'), ('venezuelan', 'Venezuelan'), ('vietnamese', 'Vietnamese'), ('yemeni', 'Yemeni'), ('zambian', 'Zambian'), ('zimbabwean', 'Zimbabwean'), ('no category', 'No Category'), ('mixed', 'Mixed')], default='other', help_text='Select the country associated with this recipe', max_length=50),
        ),
    ]