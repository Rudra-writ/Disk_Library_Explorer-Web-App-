from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from systemCodeManager.models import timeTracking
from django.contrib import messages
import datetime
import pandas as pd
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from datetime import date
import os
def showhistory(request):
    showall = timeTracking.objects.all()
    return render(request, 'index.html', {"data": showall})

def insertrecord(request):
    if (request.method == 'GET'):
        objectall = timeTracking.objects.all()
        name_lists = ['Rudra','Tommaso_Capuano', 'Jonas_Weis', 'Kiran_Chincholi', 'Juan_R._Llobet', 'Shahid_Mobin', 'Matthias_Hecht', 'Marc_Haßenpflug', 'Lucian-Mircea_Grec', 'Isaac_Lopez', 'Rishabh_Yadav', 'Prathamesh_Malpathak', 'Julian_Erdle', 'Jakob_Habermann', 'Moritz_Baur', 'Gerhard_Becker', 'Fabian_Braun', 'Sebastian_Reiter', 'Dangelo_Aniello', 'Jacob_Lawson', 'Francesc_Betorz', 'Thorben_Schmitz ', 'Geoffroy_de_Dinechin', 'Rehan_Bandara', 'Emmanuel_Telmar', 'Jean_Labuschagne', 'Alberto_Progida ', 'Adrian_Lorenz', 'Robin_Scholtes', 'Julie_Letoile ', 'Mihir_Patwardhan', 'Jacopo_Irone', 'Stefan_Brieschenk', 'Maximilian_Pfohl', 'Johann_Gogesch', 'Tobias_Drexl', 'Thomas_Mason', 'Shrinivas_Iyengar ', 'Martin_Lee', 'Titto_Ephraim_Methew', 'Calvin_Füller', 'Oliver_Hitchens', 'Brunno_B._Vasques', 'Ramzi_Aouimeur', 'Jude_Sudario', 'Giulio_Pacifici', 'Kilian_Reutter', 'Ilker_Yasar', 'Robin_Duhnsen', 'Victor_Covasan', 'Sven_Deist', 'Jannis_Bobinger', 'Jaime_Aguirre', 'Alan_Rochford', 'Matthias_Jacoby', 'Dragos_Varsescu', 'Mathieu_Rayer', 'Elia_Poli', 'Christophe_Geuens', 'Samuel_Leitenmeier ', 'Anton_Liegert', 'Stefan_Eisenknappl', 'Maximilian_Koch', 'Veronika_Pröller', 'Tomasz_Witkowski', 'Omar_Abrahams', 'Emily_Seeberg', 'Fabio_Kerstens', 'Nian_Fuls', 'Patrick_Wagner', 'Marius_Hahn', 'Ines_Pereirinha', 'Andreas_Stark', 'Dmitrii_Matias', 'Filipe_Valentim', 'Amir_Ibrahim', 'Lukas_Welzel', 'Stephan_Schmid', 'David_Maiden ', 'Vasyl_Kashevko', 'Nadine_Steck', 'Laura_Soldo', 'Mario_Araujo', 'Jyotiben_Tiwari', 'Pierre_Groslambert', 'Michael_Mair', 'Jörn_Spurmann', 'Nicholas_Tegg', 'Rolf_Wubben', 'Almero_Gerber', 'Kevin_Eppenga', 'Philipp_Becker', 'Stijn_Koehler ', 'Jonas_Gauger', 'Adem_Tosun', 'Tut_Baldock', 'Daanish_Bambery', 'Alexander_Polidar', 'Beatriz_Oliveira', 'Maximilian_Erhardt', 'Tibor_Völcker', 'Halil_Demiralan', 'Jacopo_Ventura', 'Babu_Maddukuri', 'Thomas_Wüthrich', 
'Karl_Fuchs', 'Jeije_Van_den_Wijngaart', 'Virgile_Gautier', 'Thomas_Britting', 'Sebastian_Landsmann', 'Philip_Tzonev', 'Julian_Rimer', 'Ibrahim_Ata', 'Karina_Sapelnikova', 'Jonas_Kellner ', 'Daniil_Kedrinski', 'Daniel_Kussner', 'Thomas_Barouh', 'Florian_Eisele', 'Nick_Stein', 'Paul_Haufe', 'Michael_Hörmann', 'Eric_Brunner', 'Andreas_Engel', 'Nitin_Kumar', 'Lukas_Walter ', 'Melanie_Wullaert', 'Pierpaolo_Toniato ', 'David_Abplanalp', 'Marco_Desiderio', 'Yannick_Eydner', 'Trivendra_Kulhare', 'Léo_Bulckaen', 'Naveen_Gunasekaran', 'Stefano_Luca', 'Sydney_Dupasquier', 'Olgierd_Cichorek', 'Andreas_Tumbrink', 'Navin_Subramanian ', 'Monica_Arizaga', 'Guillaume_Lortie', 'Nicola_Zappacosta', 'Filipe_Barreiro', 'Calvin_Hooton', 'Joris_Kievits', 'Malte_Hauck', 'Tiago_Spieß', 'Alan_Saucedo', 'Jakhongir_Mamadov', 'Ponnaiyan_Ramasamy', 'Johannes_Benning', 'Sebastian_Schaeffler', 'Lars_van_der_Heijden', 'Julian_Busch', 'Peter_Nothofer', 'Marios_Karanikolidis', 'Dan_Thilderkvist', 'Sandro_Schönhoff', 'Zeljko_Pavlovic', 'Stefano_Centorame', 'Stefan_Panajotovic', 'Daniel_Severinsen', 'Pjotr_Lengkeek', 'Sammy_Ma', 'Praveen_Vasan', 'Phillip_Abplanalp ', 'Atef_Ghalayini ', 'Amr_Ibrahim', 'Jonathan_Panchyrz']
        lists=  ['S1PR-E01-TPU-SEN', 'GRND-EN1-MRO', 'S1PR-E02-3PB-MIX', 'GRND-HIL-MRO', 'S2VE-SEP-REC', 'BDSM-BDX-BJS', 'GRND-SLT', 'FCLY-WS1-CON', 'S3AV-NAV-INS', 'S1PR-E02-2TP-FUP', 'GRND-STR-FRG', 'GRND-HY1-CTN-MRO', 'S1PR-E02-0GA-OXL', 'S1AV-EUS-INT-PWR', 'BDSM-BDX-RAF-NAM', 'S1VE-TCR-SNS-PTS', 'C1AZ', 'S1PR-E01-TPU-BOV', 'S2VE-PLS', 'S1AV-NDE-N01', 'GRND-SLT-OST-PMD', 'GRND-FUR', 'GRND-STR-SEP', 'S2VE-RCS', 'S1PR-E02-0GA-SST', 'S1PR-E02-1EC-TCA-RDF', 'GRND-SHK-MRO', 'S1PR-E02-4CU-410', 'S3AV', 'GRND-INJ', 'S1AV', 'BDSM-BDX-EUC-ETP', 'C1AZ-PAD-GAS', 'S1PR-E02-0GA-FUL', 'GRND-PHS-MRO', 'S2VE-SEP-PHR', 'GRND-STR-REL-MRO', 'S1VE-PRS-THP', 'S1PR-E02-3PB-RDF', 'FCLY-WS2-MAC', 'S3VE-FRG-USH', 'S1VE-TFM-VAC-USV', 'S1PR-E02-0GA-MTH', 'S1VE-TCR-ITP', 'S1VE-TCR-PMD-ASL', 'GRND-PST', 'GRND-STR-MRO', 'S3VE-KST-STR', 'S1VE-PRS-RLF', 'S1PR-E02-4CU-410-RDF', 'BDSM-BDX', 'S1PR-E02-TVC-ACT', 'S2VE-TCR-SNS-AUX', 'GRND-INT-MRO', 'S2VE-SST', 'S1VE-TFM', 'GRND-PD2', 'FCLY-WS2-CLN', 'C2FR', 'GRND-TAS-SG2', 'GRND-HY1-CLN', 'S1VE-TFM-REL', 'BDSM-BDX-EMS', 'BDSM-BDX-ESA-PD2', 'FCLY-WS2-CON', 'S1VE', 'S2PR-E02-NEX', 'GRND-TPU-STR-MRO', 'GRND-STR-VE1-MRO', 'FDPT-EMS', 'S1AV-FTS', 'S1PR-E02-1EC-RDF', 'C1AZ-OPS', 'S3VE-FRG', 'GRND-HPH-MRO', 'S1VE-SEP-PHR', 'S1PR-E02-4CU-407-RDF', 'GRND-NM1-MRO', 'FCLY-WSP', 'C5DE', 'S3PR-K01-TCA-TCH', 'C1AZ-LOG', 'S3AV-NAV', 'FCLY-WS1-PPE', 'GRND-STR-COM', 'BDSM-BDX-ESA-CST-OP3', 'S1VE-PRS-RLF-ACT', 'BDSM-SAL-AST', 'S1PR-E01-TPU-GGU', 'GRND-PDT', 'S1PR-E02-4CU-407', 'S2VE-TCR-CNE', 'FCLY-WS2-TST', 'C1AZ-PAD-LOX', 'S1PR-E02-2TP-TUM-RDF', 'FDPT-NMO-UM2', 'S1PR-E01-TPU-SSS', 'S2VE-TCR-SNS-PTS', 'BDSM-BDX-ESA-CST', 'S1PR-E02-3PB-IGN', 'FDPT-ESA-CST-FSD', 'S1PR', 'BDSM-BDX-NMO', 'S3VE-FRG-SEP-REC', 'S3VE-FRG-SEP-PHR', 'Management', 'S1PR-E02-0GA', 'S3VE-KST-TNK-PMD-FLR', 'FCLY-WS2-MAC-MRO', 'GRND-BST', 'C1AZ-PAD-LN2', 'S2VE-PRS-THP-USG', 'S2AV-WRG', 'GRND-TS1-HTS', 'S1VE-TCR', 'GRND-ELC', 'FCLY-MCC-MCS', 'S1PR-E02-1EC-TCA', 'S1AV-PWR-BAT', 'GRND-PHS', 'GRND-TAS-SG1', 'S1PR-E01-TPU-TUR', 'S2VE-TCR-ITP', 'GRND-3DP-MRO', 'GRND-TS1-HTS-TB1', 'BDSM-BDX-F9X', 'GRND-TS1-HTS-MRO', 'S2PR-E02', 'S3PR-K01-TCA', 'GRND-VAC', 'S1PR-E02-4CU-405-RDF', 'BDSM-BDX-EUC-SCI', 'C1AZ-SLV', 'BDSM-BDX-MCS', 'S1PR-E02-3PB-TCA-RDF', 'S1PR-E02-4CU-408-RDF', 'FCLY-WSP-PPE', 'S2VE-TCR-PMD', 'S1PR-E01-TPU-IGN', 'S1AV-EUS', 'GRND-INS', 'S1VE-RVY', 'GRND-STR-VE1', 'S1PR-E02-RDF', 'GRND-TPU-PTR-MRO', 'S1VE-TFM-STR', 'IT', 'C1AZ-PAD-IXF-FSP', 'S1PR-E02-3PB-MIX-RDF', 'S2AV-FTS', 'C1AZ-FLY', 'S1PR-E01', 'GRND-TVC-LDB', 'FDPT-KSP', 'S1PR-E02-4CU-COX', 'S1AV-EUS-GRD-PWR', 'S2VE-PRS-THP-SNS', 'S1VE-TCR-SNS-LVL', 'GRND-TAS-SG1-MRO', 'S3AV-PWR', 'S2VE', 'S1PR-E02', 'GRND-TPU-TRG-MRO', 'GRND-TPU-MRO', 'C4CA', 'S1PR-E02-AUX', 'S3PR-K01-TRV', 'S1VE-SEP-REC', 'S1PR-E02-4CU-409', 'S1VE-PRS-RLF-300', 'C1AZ-PAD-LPS', 'S1PR-E02-0GA-SNS', 'S2AV-COM', 'S1PR-E02-1EC', 'S3VE', 'S1AV-RTS', 'S1AV-EUS-GRD', 'GRND-HIL-SCE', 'S1VE-TCR-PMD-FLR', 'S2VE-TCR-PMD-ASL', 'S3PR', 'GRND-INT', 'GRND-HFR', 'S1PR-E02-4CU-FTS', 'S3VE-RCS-USG', 'FCLY-WS2-PPE', 'GRND-BST-MRO', 'S2PR-E02-AUX', 'S2AV-EUS', 'S2VE-RCS-USG', 'S1AV-PWR', 'S1VE-TCR-ASK', 'S1PR-E02-4CU-411', 'S2VE-TCR-BSF', 'S2VE-PRS-THP-HES', 'S3VE-KST-TNK-PMD-AVX', 'GRND-SHK', 'GRND-STR-REL', 'S3VE-FRG-SEP-ACT', 'GRND-STR-COM-MRO', 'S3AV-COM', 'GRND-TPU', 'S3AV-NDE', 'S2AV', 'GRND-INS-MRO', 'S1PR-E02-1EC-MIX-RDF', 'S3VE-KST-SNS', 'GRND-TAS-SG2-MRO', 'S1PR-E01-TPU-SEL', 'S1VE-TCR-SNS', 'C1AZ-DGS', 'FCLY-WS2-PRO', 'S3AV-WRG', 'S1AV-NDE', 'S1VE-TCR-FSK', 'S1PR-E01-TCA', 'C1NO-PAD', 'S2PR', 'S1VE-PRS-RLF-200 ', 'S1AV-WRG', 'S1PR-E02-TVC-MTH', 'C1NO-LIC', 'S3VE-SEP-REC', 'BDSM-BDX-BAY', 'GRND-3DP', 'S1AV-EUS-INT', 'GRND-TAS-SWG-MRO', 'BDSM-MKT', 'GRND-SNS-PSS', 'S3VE-KST-USS', 'GRND-HPH', 'FDPT-ESA', 'BDSM-BDX-RAF-CCT', 'FCLY-IT-ITI ', 'GRND-TS1-VTS-IST', 'FCLY-SSC', 'GRND-SLT-OST-PMD-FLR', 'S3PR-K01-TVC', 'BDSM-BDX-RAF', 'GRND-TS1', 'S3VE-FRG-ITP', 'BDSM-BDX-ESA-FAM', 'S1VE-SEP-ACT', 'S1PR-E02-2TP', 'S3AV-EUS', 'GRND-TS1-VTS-MRO', 'GRND-TS1-HTS-TB1-PFT', 'GRND-VAC-MRO', 'S2VE-SEP-ACT', 'S1VE-PLS-USR', 'BDSM-MKT-SMX', 'BDSM-BDX-ESA-CST-OP2', 'S2VE-TCR-TFM', 'S1VE-PRS-THP-HES', 'S2AV-NDE', 'S1VE-PLS-USC', 'BDSM-MKT-WEB', 'BDSM-BDX-EUC', 'S1PR-E02-4CU-408', 'S1PR-E02-0GA-GDT', 'S1VE-TCR-TSF', 'FCLY-IT-USR ', 'BDSM-BDX-EUC-LCL', 'GRND-CRS', 'C1AZ-PAD', 'GRND-HY1-HST', 'GRND-STR-SEP-MRO', 'S1PR-E02-0GA-OXL-APD', 'C6OM', 'S3VE-KST-HES', 'S3VE-KST-USG', 'GRND-SNS-MRO', 'FDPT-NMO', 'S2VE-TCR-STR', 'S1PR-E02-4CU-402-RDF', 'BDSM-SAL-OIT', 'S3AV-NAV-TSO', 'S1VE-SEP', 'BDSM-MKT-SYM', 'S1PR-E02-1EC-IGN', 'C1NO-FLY', 'BDSM-SAL-PIM', 'S1PR-E02-4CU-405', 'S3VE-KST-TNK', 'S2VE-PRS-THP', 'S2VE-TCR-SNS', 'S2VE-PLS-MCV', 'FCLY-WS2', 'GRND-HY1-CTN', 'S1PR-E02-AUX-RDF', 'FCLY-C1 ', 'FDPT-AWO', 'S3VE-KST-TNK-PMD-ASL', 'GRND-TS1-VTS-IEQ', 'S1PR-E02-0GA-HTS', 'S1PR-E02-3PB', 'BDSM-SAL', 'S1VE-PLS-MCV', 'GRND-TPU-PTR', 'GRND-STR-KST-MRO', 'FDPT-MCS', 'S1AV-COM', 'S1PR-E02-3PB-IGN-RDF', 'S3PR-K01-TCA-INJ', 'GRND-TVC-MRO', 'S1PR-E02-4CU-402', 'S3VE-FRG-SNS', 'GRND-HFR-MRO', 'GRND-TPU-STR', 'S1PR-E01-TPU-CLT', 'GRND-TPU-TRG', 'FDPT-ESA-LCA', 'S1VE-TFM-SST', 'S1PR-E02-2TP-OXP', 'S1PR-E02-0GA-PVC', 'S1PR-E02-TVC-PWR', 'C2FR-FLY', 'FCLY-WSP-OFF', 'C1NO', 'S1PR-E02-4CU-406', 'S2VE-TCR-PMD-AVX', 'FCLY-WS2-REL', 'S1PR-E02-0GA-IGN', 'S1VE-TFM-USH', 'GRND-TS1-VTS', 'GRND-PST-MRO', 'S1VE-PRS-THP-USG', 'S1AV-RVY', 'S1VE-TFM-VAC', 'BDSM-BDX-ESA-CST-FP1', 'S3AV-RFS', 'C2FR-GRY', 'BDSM-BDX-NMO-EL3', 'S1PR-E02-4CU-401', 'GRND-NM1', 'GRND-TS1-HTX-MRO', 'FCLY-TC1', 'S1VE-TCR-SNS-AUX', 'BDSM-SAL-CLS', 'BDSM-BDX-RAF-CBP', 'BDSM-SAL-RAY', 'S2VE-PRS-REG', 'S3VE-DSP', 'C1AZ-PAD-WDS', 'S2AV-PWR', 'C1AZ-PAD-AIF', 'S1VE-PRS-THP-SNS', 'S2VE-TCR-TSF', 'S1PR-E02-ECU', 'FCLY-WSP-PRO', 'GRND-HY1-MRO', 'FDPT-ESA-CST-OSD', 'FCLY-IT ', 'GRND-TVC', 'GRND-EN1', 'BDSM-BDX-RAF-TPB', 'S3VE-FRG-FLR', 'GRND-HY1', 'S1PR-E02-1EC-IGN-RDF', 'S1PR-E02-TVC-GIM', 'S1PR-E02-0GA-PUL', 'S3VE-SEP-ACT', 'GRND-TS1-HTS-TB1-PWP', 'BDSM-BDX-ESA', 'S1PR-E02-0GA-GEJ', 'C7UK', 'S1PR-E02-0GA-PRS', 'S1PR-E01-TPU', 'S2VE-TCR-SNS-LVL', 'C1AZ-LCC', 'S1PR-E02-4CU-403-RDF', 'C1AZ-PAD-IXF', 'S1VE-PRS', 'S1VE-TCR-PMD', 'S1VE-PRS-REG', 'BDSM-BDX-KSP', 'GRND-HIL', 'C1AZ-SEA', 'S3VE-KST-ITP', 'GRND-SLT-IST', 'S1VE-PLS', 'S3VE-FRG-SEP', 'S3VE-KST', 'S3VE-SEP-PHR', 'FCLY-WS2-ELC', 'GRND-TAS-MRO', 'S2VE-PRS-RLF', 'C1', 'S3AV-FCS', 'S2VE-PLS-USC', 'GRND-TS1-HTX', 'GRND-TS1-MRO', 'S2VE-TCR', 'GRND-PD2-MRO', 'BDSM-BDX-ESA-CST-OP1', 'GRND-INJ-MRO', 'FCLY-WSP-CON', 'S3VE-SEP',  'GRND-STR', 'GRND-FUR-MRO', 'S1VE-TCR-STR', 'S2VE-PLS-USR', 'GRND-STR-KST', 'GRND-SLT-HEX', 'GRND-TAS', 'BDSM-BDX-ESA-LCA', 'GRND-SNS', 'GRND-TAS-SWG', 'GRND-PDT-MRO', 'C2FR-OPS', 'C1AZ-PAD-ERC', 'S1PR-E02-3PB-TCA', 'S1VE-TCR-FSK-USH', 'BDSM-MKT-EVT', 'GRND-STR-FRG-MRO', 'C1NO-IXF', 'S1PR-E02-4CU-403', 'S3VE-RCS', 'FCLY-MCC', 'GRND-HY1-CLN-MRO', 'BDSM-BDX-AIC', 'GRND-HY1-HST-MRO', 'S3VE-FRG-STR', 'S3VE-KST-SAB', 'FDPT-ESA-CST', 'BDSM-SAL-PUG', 'FDPT-AIC', 'S1AV-EUS-INT-COM', 'GRND-SLT-OST-PMD-AVX', 'S3PR-K01-TCA-IGN', 'C1AZ-GRY', 'S1PR-E02-0GA-GDT-RDF', 'C1AZ-PAD-UM1', 'S3AV-NAV-SIM', 'S1PR-E01-TPU-PMP', 'S2VE-PRS', 'S1VE-TCR-PMD-AVX', 'FDPT-ESA-NST', 'BDSM-SAL-OSE', 'GRND-SLT-OST', 'BDSM-BDX-RAF-REM', 'S1PR-E02-4CU-404', 'GRND-NM1-DAQ', 'S2VE-TCR-PMD-FLR', 'BDSM-BDX-EUC-HEU', 'S1PR-E02-4CU', 'FCLY-WS2-OFF', 'S3VE-KST-TNK-PMD', 'S2VE-SEP', 'FCLY-WS1', 'GRND-SLT-OST-PMD-ASL', 'S1AV-EUS-GRD-COM', 'S3PR-K01', 'S1PR-E02-1EC-MIX', 'S1PR-E02-SLE', 'S1PR-E02-TVC', 'BDSM-BDX-NMO-UM2', 'S1VE-TFM-SST-USS', 'S1PR-E02-2TP-TUM']
        d_phases =['Test', 'Purchasing/Sourcing', 'Analysis', 'Design_(CAD)', 'Systems_Engineering', 'Assembling', 'Management']
        
        departments = ['Propulsion', 'Avionic', 'Vehicle', 'Test', 'BD/Marketing', 'Production', 'Finance', 'Launch', 'PM', 'GNC', '3D_Printing']
        projects = ['FDPT-NMO-UM2', 'FDPT-ESA-CST', 'FDPT-ESA-CST-FSD', 'FDPT-ESA-CST-OSD', 'FDPT-AWO', 'FDPT-EMS', 'FDPT-ESA', 'FDPT-MCS', 'FDPT-ESA-NST', 'FDPT-NMO', 'FDPT-AIC', 'FDPT-KSP', 'FDPT-ESA-LCA']
        if request.GET.get('empname') and request.GET.get('department') and request.GET.get('currentweek')   and ((request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1')) or (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) or (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3')) or (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) or (request.GET.get('day5')  and request.GET.get('systemcode5') and request.GET.get('time_worked5')) or (request.GET.get('day6')  and request.GET.get('systemcode6') and request.GET.get('time_worked6'))):
            if (request.GET.get('empname') in timeTracking.objects.values_list('empname', flat=True)):
               messages.success(request, "You are already registered. Please go back and use the link for a new record!")
               return render(request, 'insert.html') 
            elif (request.GET.get('empname') not in name_lists):
               messages.success(request, "Invalid name!! Please select your name from the list.")
               return render(request, 'insert.html') 
                
            
            else:
                 d_phases =['Test', 'Purchasing/Sourcing', 'Analysis', 'Design_(CAD)', 'Systems_Engineering', 'Assembling', 'Management']
        
                 departments = ['Propulsion', 'Avionic', 'Vehicle', 'Test', 'BD/Marketing', 'Production', 'Finance', 'Launch', 'PM', 'GNC', '3D_Printing']
                 projects = ['FDPT-NMO-UM2', 'FDPT-ESA-CST', 'FDPT-ESA-CST-FSD', 'FDPT-ESA-CST-OSD', 'FDPT-AWO', 'FDPT-EMS', 'FDPT-ESA', 'FDPT-MCS', 'FDPT-ESA-NST', 'FDPT-NMO', 'FDPT-AIC', 'FDPT-KSP', 'FDPT-ESA-LCA']

                 saverecord = timeTracking()
                 saverecord.empname = request.GET.get('empname')
                 if (request.GET.get('department') in departments):
                   saverecord.department = request.GET.get('department')
                 else:
                     messages.success(request, "Invalid department!! Please select your department from the list.")
                     return render(request, 'insert.html') 

                 saverecord.currentweek = request.GET.get('currentweek')
                 

                 if(request.GET.get('add1') and request.GET.get('day1') != '' and request.GET.get('systemcode1') in lists and (request.GET.get('development_phase1') in d_phases  or request.GET.get('development_phase1') == '') and (request.GET.get('project1') in projects or request.GET.get('project1') == '' )):
                    d1 = request.GET.get('day1')
                    saverecord.day1 = datetime.datetime.strptime(d1, "%d/%m/%Y").date()
                    saverecord.systemcode1 = request.GET.get('systemcode1')
                    saverecord.time_worked1 = request.GET.get('time_worked1')
                    saverecord.development_phase1 = request.GET.get('development_phase1')
                    saverecord.project1 = request.GET.get('project1')
                   

                 elif (request.GET.get('add2') and request.GET.get('day2') != '' and request.GET.get ('systemcode2') in lists and (request.GET.get('development_phase2') in d_phases or request.GET.get('development_phase2') == '')  and (request.GET.get('project2') in projects or request.GET.get('project2') == '' ) ):
                    d2 = request.GET.get('day2')
                    saverecord.day1 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                    saverecord.systemcode2 = request.GET.get('systemcode2')
                    saverecord.time_worked2 = request.GET.get('time_worked2')
                    saverecord.development_phase2 = request.GET.get('development_phase2')
                    saverecord.project2 = request.GET.get('project2')

                 elif (request.GET.get('add3') and request.GET.get('day3') != '' and request.GET.get ('systemcode3') in lists and (request.GET.get('development_phase3') in d_phases or request.GET.get('development_phase3') == '')  and (request.GET.get('project3') in projects or request.GET.get('project3') == '' )):
                     d3 = request.GET.get('day3')
                     saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                     saverecord.time_worked3 = request.GET.get('time_worked3')
                     saverecord.systemcode3 = request.GET.get('systemcode3')
                     saverecord.development_phase3 = request.GET.get('development_phase3')
                     saverecord.project3 = request.GET.get('project3')

                 elif (request.GET.get('add4') and request.GET.get('day4') != '' and request.GET.get ('systemcode4') in lists and (request.GET.get('development_phase4') in d_phases or request.GET.get('development_phase4') == '')  and (request.GET.get('project4') in projects or request.GET.get('project4') == '')):
                     d4 = request.GET.get('day4')
                     saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                     saverecord.time_worked4 = request.GET.get('time_worked4')
                     saverecord.systemcode4 = request.GET.get('systemcode4')
                     saverecord.development_phase4 = request.GET.get('development_phase4')
                     saverecord.project4 = request.GET.get('project4')
                 

                 elif (request.GET.get('add5') and request.GET.get('day5') != '' and request.GET.get ('systemcode5') in lists and (request.GET.get('development_phase5') in d_phases or request.GET.get('development_phase5') == '')  and (request.GET.get('project5') in projects or request.GET.get('project5') == '' )):
                     d5 = request.GET.get('day5')
                     saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                     saverecord.time_worked5 = request.GET.get('time_worked5')
                     saverecord.systemcode5 = request.GET.get('systemcode5')
                     saverecord.development_phase5 = request.GET.get('development_phase5')
                     saverecord.project5 = request.GET.get('project5')

                 elif (request.GET.get('add6') and request.GET.get('day6') != '' and request.GET.get ('systemcode6') in lists and (request.GET.get('development_phase6') in d_phases or request.GET.get('development_phase6') == '') and (request.GET.get('project6') in projects or request.GET.get('project6') == '')):
                     d6 = request.GET.get('day6')
                     saverecord.day6 = datetime.datetime.strptime(d6, "%d/%m/%Y").date()
                     saverecord.time_worked6 = request.GET.get('time_worked6')
                     saverecord.systemcode6 = request.GET.get('systemcode6')
                     saverecord.development_phase1 = request.GET.get('development_phase6')
                     saverecord.project1 = request.GET.get('project6')

                 else:
                     saverecord.day1 = None
                     saverecord.time_worked1 = None
                     saverecord.development_phase1 = None
                     saverecord.project1 = None

                     saverecord.day2 = None
                     saverecord.time_worked2 = None
                     saverecord.development_phase2 = None
                     saverecord.project2 = None

                     saverecord.day3 = None
                     saverecord.time_worked3 = None
                     saverecord.development_phase3 = None
                     saverecord.project3 = None

                     saverecord.day4 = None
                     saverecord.time_worked4 = None
                     saverecord.development_phase4 = None
                     saverecord.project4 = None

                     saverecord.day5 = None
                     saverecord.time_worked5 = None
                     saverecord.development_phase5 = None
                     saverecord.project5 = None


                     saverecord.day6 = None
                     saverecord.time_worked6 = None
                     saverecord.development_phase6 = None
                     saverecord.project6 = None
                     

                     saverecord.systemcode1 = None
                     saverecord.systemcode2 = None
                     saverecord.systemcode3 = None
                     saverecord.systemcode4 = None
                     saverecord.systemcode5 = None
                     now = datetime.datetime.now()
                     today = (now.strftime("%A"))
                     week = datetime.datetime.now().isocalendar()[1]
                     if (today == "Monday"):
                        first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                     elif (today == "Tuesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                     elif (today == "Wednesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                     elif (today == "Thursday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                     elif (today == "Friday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                     elif (today == "Saturday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                     else:

                        first_day = None
                        second_day = None
                        third_day = None
                        fourth_day = None
                        fifth_day = None
                        sixth_day = None
                     messages.success(request, "Error: Please make sure the Department,Development phase, Project and System Codes are selected from the list and the dates belong to the current week!!")
                     return render(request, 'insert.html', {"data": objectall, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})
                 
                 now = datetime.datetime.now()
                 today = (now.strftime("%A"))
                 week = datetime.datetime.now().isocalendar()[1]
                 if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                 elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                 elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                 elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                 elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                 elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                 else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None
                 if ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):
                    saverecord.save()
                    messages.success(request, "Data saved successfully !!")              
                    return render(request, 'insert.html', {"data": objectall, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})
                 else:
                     messages.success(request, "Error: Please make sure the Department, Development phase, Project and System Codes are selected from the list and the dates belong to the current week!!")
                     return render(request, 'insert.html', {"data": objectall, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})
    
        else:   
                now = datetime.datetime.now()
                today = (now.strftime("%A"))
                week = datetime.datetime.now().isocalendar()[1]
                if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None
                
                messages.success(request, "One of the mandatory fields is missing...")
                return render(request, 'insert.html', {"data": objectall, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})
    else:
        return render(request, 'insert.html')





def firstpage(request):
    if (request.method == 'POST'):
        
       if request.POST.get('name'):
            thisname = request.POST.get('name')
            new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [thisname])

       elif request.POST.get('employeename'):
            thisname = request.POST.get('employeename')
            objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [thisname])
            return render(request, 'index.html', {"data" :objects})
       else:
            return render(request, 'firstpage.html' )
    else:
        return render(request, 'firstpage.html' )

            
def insert_record(request):
   
   
    if (request.method == 'GET'):
        

        lists=  ['S1PR-E01-TPU-SEN', 'GRND-EN1-MRO', 'S1PR-E02-3PB-MIX', 'GRND-HIL-MRO', 'S2VE-SEP-REC', 'BDSM-BDX-BJS', 'GRND-SLT', 'FCLY-WS1-CON', 'S3AV-NAV-INS', 'S1PR-E02-2TP-FUP', 'GRND-STR-FRG', 'GRND-HY1-CTN-MRO', 'S1PR-E02-0GA-OXL', 'S1AV-EUS-INT-PWR', 'BDSM-BDX-RAF-NAM', 'S1VE-TCR-SNS-PTS', 'C1AZ', 'S1PR-E01-TPU-BOV', 'S2VE-PLS', 'S1AV-NDE-N01', 'GRND-SLT-OST-PMD', 'GRND-FUR', 'GRND-STR-SEP', 'S2VE-RCS', 'S1PR-E02-0GA-SST', 'S1PR-E02-1EC-TCA-RDF', 'GRND-SHK-MRO', 'S1PR-E02-4CU-410', 'S3AV', 'GRND-INJ', 'S1AV', 'BDSM-BDX-EUC-ETP', 'C1AZ-PAD-GAS', 'S1PR-E02-0GA-FUL', 'GRND-PHS-MRO', 'S2VE-SEP-PHR', 'GRND-STR-REL-MRO', 'S1VE-PRS-THP', 'S1PR-E02-3PB-RDF', 'FCLY-WS2-MAC', 'S3VE-FRG-USH', 'S1VE-TFM-VAC-USV', 'S1PR-E02-0GA-MTH', 'S1VE-TCR-ITP', 'S1VE-TCR-PMD-ASL', 'GRND-PST', 'GRND-STR-MRO', 'S3VE-KST-STR', 'S1VE-PRS-RLF', 'S1PR-E02-4CU-410-RDF', 'BDSM-BDX', 'S1PR-E02-TVC-ACT', 'S2VE-TCR-SNS-AUX', 'GRND-INT-MRO', 'S2VE-SST', 'S1VE-TFM', 'GRND-PD2', 'FCLY-WS2-CLN', 'C2FR', 'GRND-TAS-SG2', 'GRND-HY1-CLN', 'S1VE-TFM-REL', 'BDSM-BDX-EMS', 'BDSM-BDX-ESA-PD2', 'FCLY-WS2-CON', 'S1VE', 'S2PR-E02-NEX', 'GRND-TPU-STR-MRO', 'GRND-STR-VE1-MRO', 'FDPT-EMS', 'S1AV-FTS', 'S1PR-E02-1EC-RDF', 'C1AZ-OPS', 'S3VE-FRG', 'GRND-HPH-MRO', 'S1VE-SEP-PHR', 'S1PR-E02-4CU-407-RDF', 'GRND-NM1-MRO', 'FCLY-WSP', 'C5DE', 'S3PR-K01-TCA-TCH', 'C1AZ-LOG', 'S3AV-NAV', 'FCLY-WS1-PPE', 'GRND-STR-COM', 'BDSM-BDX-ESA-CST-OP3', 'S1VE-PRS-RLF-ACT', 'BDSM-SAL-AST', 'S1PR-E01-TPU-GGU', 'GRND-PDT', 'S1PR-E02-4CU-407', 'S2VE-TCR-CNE', 'FCLY-WS2-TST', 'C1AZ-PAD-LOX', 'S1PR-E02-2TP-TUM-RDF', 'FDPT-NMO-UM2', 'S1PR-E01-TPU-SSS', 'S2VE-TCR-SNS-PTS', 'BDSM-BDX-ESA-CST', 'S1PR-E02-3PB-IGN', 'FDPT-ESA-CST-FSD', 'S1PR', 'BDSM-BDX-NMO', 'S3VE-FRG-SEP-REC', 'S3VE-FRG-SEP-PHR', 'Management', 'S1PR-E02-0GA', 'S3VE-KST-TNK-PMD-FLR', 'FCLY-WS2-MAC-MRO', 'GRND-BST', 'C1AZ-PAD-LN2', 'S2VE-PRS-THP-USG', 'S2AV-WRG', 'GRND-TS1-HTS', 'S1VE-TCR', 'GRND-ELC', 'FCLY-MCC-MCS', 'S1PR-E02-1EC-TCA', 'S1AV-PWR-BAT', 'GRND-PHS', 'GRND-TAS-SG1', 'S1PR-E01-TPU-TUR', 'S2VE-TCR-ITP', 'GRND-3DP-MRO', 'GRND-TS1-HTS-TB1', 'BDSM-BDX-F9X', 'GRND-TS1-HTS-MRO', 'S2PR-E02', 'S3PR-K01-TCA', 'GRND-VAC', 'S1PR-E02-4CU-405-RDF', 'BDSM-BDX-EUC-SCI', 'C1AZ-SLV', 'BDSM-BDX-MCS', 'S1PR-E02-3PB-TCA-RDF', 'S1PR-E02-4CU-408-RDF', 'FCLY-WSP-PPE', 'S2VE-TCR-PMD', 'S1PR-E01-TPU-IGN', 'S1AV-EUS', 'GRND-INS', 'S1VE-RVY', 'GRND-STR-VE1', 'S1PR-E02-RDF', 'GRND-TPU-PTR-MRO', 'S1VE-TFM-STR', 'IT', 'C1AZ-PAD-IXF-FSP', 'S1PR-E02-3PB-MIX-RDF', 'S2AV-FTS', 'C1AZ-FLY', 'S1PR-E01', 'GRND-TVC-LDB', 'FDPT-KSP', 'S1PR-E02-4CU-COX', 'S1AV-EUS-GRD-PWR', 'S2VE-PRS-THP-SNS', 'S1VE-TCR-SNS-LVL', 'GRND-TAS-SG1-MRO', 'S3AV-PWR', 'S2VE', 'S1PR-E02', 'GRND-TPU-TRG-MRO', 'GRND-TPU-MRO', 'C4CA', 'S1PR-E02-AUX', 'S3PR-K01-TRV', 'S1VE-SEP-REC', 'S1PR-E02-4CU-409', 'S1VE-PRS-RLF-300', 'C1AZ-PAD-LPS', 'S1PR-E02-0GA-SNS', 'S2AV-COM', 'S1PR-E02-1EC', 'S3VE', 'S1AV-RTS', 'S1AV-EUS-GRD', 'GRND-HIL-SCE', 'S1VE-TCR-PMD-FLR', 'S2VE-TCR-PMD-ASL', 'S3PR', 'GRND-INT', 'GRND-HFR', 'S1PR-E02-4CU-FTS', 'S3VE-RCS-USG', 'FCLY-WS2-PPE', 'GRND-BST-MRO', 'S2PR-E02-AUX', 'S2AV-EUS', 'S2VE-RCS-USG', 'S1AV-PWR', 'S1VE-TCR-ASK', 'S1PR-E02-4CU-411', 'S2VE-TCR-BSF', 'S2VE-PRS-THP-HES', 'S3VE-KST-TNK-PMD-AVX', 'GRND-SHK', 'GRND-STR-REL', 'S3VE-FRG-SEP-ACT', 'GRND-STR-COM-MRO', 'S3AV-COM', 'GRND-TPU', 'S3AV-NDE', 'S2AV', 'GRND-INS-MRO', 'S1PR-E02-1EC-MIX-RDF', 'S3VE-KST-SNS', 'GRND-TAS-SG2-MRO', 'S1PR-E01-TPU-SEL', 'S1VE-TCR-SNS', 'C1AZ-DGS', 'FCLY-WS2-PRO', 'S3AV-WRG', 'S1AV-NDE', 'S1VE-TCR-FSK', 'S1PR-E01-TCA', 'C1NO-PAD', 'S2PR', 'S1VE-PRS-RLF-200 ', 'S1AV-WRG', 'S1PR-E02-TVC-MTH', 'C1NO-LIC', 'S3VE-SEP-REC', 'BDSM-BDX-BAY', 'GRND-3DP', 'S1AV-EUS-INT', 'GRND-TAS-SWG-MRO', 'BDSM-MKT', 'GRND-SNS-PSS', 'S3VE-KST-USS', 'GRND-HPH', 'FDPT-ESA', 'BDSM-BDX-RAF-CCT', 'FCLY-IT-ITI ', 'GRND-TS1-VTS-IST', 'FCLY-SSC', 'GRND-SLT-OST-PMD-FLR', 'S3PR-K01-TVC', 'BDSM-BDX-RAF', 'GRND-TS1', 'S3VE-FRG-ITP', 'BDSM-BDX-ESA-FAM', 'S1VE-SEP-ACT', 'S1PR-E02-2TP', 'S3AV-EUS', 'GRND-TS1-VTS-MRO', 'GRND-TS1-HTS-TB1-PFT', 'GRND-VAC-MRO', 'S2VE-SEP-ACT', 'S1VE-PLS-USR', 'BDSM-MKT-SMX', 'BDSM-BDX-ESA-CST-OP2', 'S2VE-TCR-TFM', 'S1VE-PRS-THP-HES', 'S2AV-NDE', 'S1VE-PLS-USC', 'BDSM-MKT-WEB', 'BDSM-BDX-EUC', 'S1PR-E02-4CU-408', 'S1PR-E02-0GA-GDT', 'S1VE-TCR-TSF', 'FCLY-IT-USR ', 'BDSM-BDX-EUC-LCL', 'GRND-CRS', 'C1AZ-PAD', 'GRND-HY1-HST', 'GRND-STR-SEP-MRO', 'S1PR-E02-0GA-OXL-APD', 'C6OM', 'S3VE-KST-HES', 'S3VE-KST-USG', 'GRND-SNS-MRO', 'FDPT-NMO', 'S2VE-TCR-STR', 'S1PR-E02-4CU-402-RDF', 'BDSM-SAL-OIT', 'S3AV-NAV-TSO', 'S1VE-SEP', 'BDSM-MKT-SYM', 'S1PR-E02-1EC-IGN', 'C1NO-FLY', 'BDSM-SAL-PIM', 'S1PR-E02-4CU-405', 'S3VE-KST-TNK', 'S2VE-PRS-THP', 'S2VE-TCR-SNS', 'S2VE-PLS-MCV', 'FCLY-WS2', 'GRND-HY1-CTN', 'S1PR-E02-AUX-RDF', 'FCLY-C1 ', 'FDPT-AWO', 'S3VE-KST-TNK-PMD-ASL', 'GRND-TS1-VTS-IEQ', 'S1PR-E02-0GA-HTS', 'S1PR-E02-3PB', 'BDSM-SAL', 'S1VE-PLS-MCV', 'GRND-TPU-PTR', 'GRND-STR-KST-MRO', 'FDPT-MCS', 'S1AV-COM', 'S1PR-E02-3PB-IGN-RDF', 'S3PR-K01-TCA-INJ', 'GRND-TVC-MRO', 'S1PR-E02-4CU-402', 'S3VE-FRG-SNS', 'GRND-HFR-MRO', 'GRND-TPU-STR', 'S1PR-E01-TPU-CLT', 'GRND-TPU-TRG', 'FDPT-ESA-LCA', 'S1VE-TFM-SST', 'S1PR-E02-2TP-OXP', 'S1PR-E02-0GA-PVC', 'S1PR-E02-TVC-PWR', 'C2FR-FLY', 'FCLY-WSP-OFF', 'C1NO', 'S1PR-E02-4CU-406', 'S2VE-TCR-PMD-AVX', 'FCLY-WS2-REL', 'S1PR-E02-0GA-IGN', 'S1VE-TFM-USH', 'GRND-TS1-VTS', 'GRND-PST-MRO', 'S1VE-PRS-THP-USG', 'S1AV-RVY', 'S1VE-TFM-VAC', 'BDSM-BDX-ESA-CST-FP1', 'S3AV-RFS', 'C2FR-GRY', 'BDSM-BDX-NMO-EL3', 'S1PR-E02-4CU-401', 'GRND-NM1', 'GRND-TS1-HTX-MRO', 'FCLY-TC1', 'S1VE-TCR-SNS-AUX', 'BDSM-SAL-CLS', 'BDSM-BDX-RAF-CBP', 'BDSM-SAL-RAY', 'S2VE-PRS-REG', 'S3VE-DSP', 'C1AZ-PAD-WDS', 'S2AV-PWR', 'C1AZ-PAD-AIF', 'S1VE-PRS-THP-SNS', 'S2VE-TCR-TSF', 'S1PR-E02-ECU', 'FCLY-WSP-PRO', 'GRND-HY1-MRO', 'FDPT-ESA-CST-OSD', 'FCLY-IT ', 'GRND-TVC', 'GRND-EN1', 'BDSM-BDX-RAF-TPB', 'S3VE-FRG-FLR', 'GRND-HY1', 'S1PR-E02-1EC-IGN-RDF', 'S1PR-E02-TVC-GIM', 'S1PR-E02-0GA-PUL', 'S3VE-SEP-ACT', 'GRND-TS1-HTS-TB1-PWP', 'BDSM-BDX-ESA', 'S1PR-E02-0GA-GEJ', 'C7UK', 'S1PR-E02-0GA-PRS', 'S1PR-E01-TPU', 'S2VE-TCR-SNS-LVL', 'C1AZ-LCC', 'S1PR-E02-4CU-403-RDF', 'C1AZ-PAD-IXF', 'S1VE-PRS', 'S1VE-TCR-PMD', 'S1VE-PRS-REG', 'BDSM-BDX-KSP', 'GRND-HIL', 'C1AZ-SEA', 'S3VE-KST-ITP', 'GRND-SLT-IST', 'S1VE-PLS', 'S3VE-FRG-SEP', 'S3VE-KST', 'S3VE-SEP-PHR', 'FCLY-WS2-ELC', 'GRND-TAS-MRO', 'S2VE-PRS-RLF', 'C1', 'S3AV-FCS', 'S2VE-PLS-USC', 'GRND-TS1-HTX', 'GRND-TS1-MRO', 'S2VE-TCR', 'GRND-PD2-MRO', 'BDSM-BDX-ESA-CST-OP1', 'GRND-INJ-MRO', 'FCLY-WSP-CON', 'S3VE-SEP',  'GRND-STR', 'GRND-FUR-MRO', 'S1VE-TCR-STR', 'S2VE-PLS-USR', 'GRND-STR-KST', 'GRND-SLT-HEX', 'GRND-TAS', 'BDSM-BDX-ESA-LCA', 'GRND-SNS', 'GRND-TAS-SWG', 'GRND-PDT-MRO', 'C2FR-OPS', 'C1AZ-PAD-ERC', 'S1PR-E02-3PB-TCA', 'S1VE-TCR-FSK-USH', 'BDSM-MKT-EVT', 'GRND-STR-FRG-MRO', 'C1NO-IXF', 'S1PR-E02-4CU-403', 'S3VE-RCS', 'FCLY-MCC', 'GRND-HY1-CLN-MRO', 'BDSM-BDX-AIC', 'GRND-HY1-HST-MRO', 'S3VE-FRG-STR', 'S3VE-KST-SAB', 'FDPT-ESA-CST', 'BDSM-SAL-PUG', 'FDPT-AIC', 'S1AV-EUS-INT-COM', 'GRND-SLT-OST-PMD-AVX', 'S3PR-K01-TCA-IGN', 'C1AZ-GRY', 'S1PR-E02-0GA-GDT-RDF', 'C1AZ-PAD-UM1', 'S3AV-NAV-SIM', 'S1PR-E01-TPU-PMP', 'S2VE-PRS', 'S1VE-TCR-PMD-AVX', 'FDPT-ESA-NST', 'BDSM-SAL-OSE', 'GRND-SLT-OST', 'BDSM-BDX-RAF-REM', 'S1PR-E02-4CU-404', 'GRND-NM1-DAQ', 'S2VE-TCR-PMD-FLR', 'BDSM-BDX-EUC-HEU', 'S1PR-E02-4CU', 'FCLY-WS2-OFF', 'S3VE-KST-TNK-PMD', 'S2VE-SEP', 'FCLY-WS1', 'GRND-SLT-OST-PMD-ASL', 'S1AV-EUS-GRD-COM', 'S3PR-K01', 'S1PR-E02-1EC-MIX', 'S1PR-E02-SLE', 'S1PR-E02-TVC', 'BDSM-BDX-NMO-UM2', 'S1VE-TFM-SST-USS', 'S1PR-E02-2TP-TUM']
        d_phases =['Test', 'Purchasing/Sourcing', 'Analysis', 'Design_(CAD)', 'Systems_Engineering', 'Assembling', 'Management']
        
        departments = ['Propulsion', 'Avionic', 'Vehicle', 'Test', 'BD/Marketing', 'Production', 'Finance', 'Launch', 'PM', 'GNC', '3D_Printing']
        projects = ['FDPT-NMO-UM2', 'FDPT-ESA-CST', 'FDPT-ESA-CST-FSD', 'FDPT-ESA-CST-OSD', 'FDPT-AWO', 'FDPT-EMS', 'FDPT-ESA', 'FDPT-MCS', 'FDPT-ESA-NST', 'FDPT-NMO', 'FDPT-AIC', 'FDPT-KSP', 'FDPT-ESA-LCA']
        
        
        empname = request.GET.get('empname')
        thisweek = request.GET.get('currentweek')
        tw1 = timeTracking.objects.raw( 'SELECT id, time_worked1 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
        tw2 = timeTracking.objects.raw( 'SELECT id, time_worked2 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
        tw3 = timeTracking.objects.raw( 'SELECT id, time_worked3 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
        tw4 = timeTracking.objects.raw( 'SELECT id, time_worked4 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
        tw5 = timeTracking.objects.raw( 'SELECT id, time_worked5 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
        tw6 = timeTracking.objects.raw( 'SELECT id, time_worked6 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])

        Total_tw1 = 0
        Total_tw2 = 0
        Total_tw3 = 0
        Total_tw4 = 0
        Total_tw5 = 0
        Total_tw6 = 0
        for t in tw1:
            if (t.time_worked1 != None):
                 Total_tw1 = t.time_worked1 + Total_tw1
        for t in tw2:
            if (t.time_worked2 != None):
                 Total_tw2 = t.time_worked2 + Total_tw2
        for t in tw3:
            if (t.time_worked3 != None):
                 Total_tw3 = t.time_worked3 + Total_tw3
        for t in tw4:
            if (t.time_worked4 != None):
                 Total_tw4 = t.time_worked4 + Total_tw4
        for t in tw5:
            if (t.time_worked5 != None):
                 Total_tw5 = t.time_worked5 + Total_tw5
        for t in tw6:
            if (t.time_worked6 != None):
                 Total_tw6 = t.time_worked6 + Total_tw6
        
        if request.GET.get('empname') and request.GET.get('push')  :
            if (request.GET.get('empname') in timeTracking.objects.values_list('empname', flat=True)):
                thisname = request.GET.get('empname')
                objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [thisname])
                now = datetime.datetime.now()
                today = (now.strftime("%A"))
                week = datetime.datetime.now().isocalendar()[1]
                if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None




                return render(request, 'insert_record.html', {"name": thisname, "data": objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})
            else:
                 messages.success(request, "Name not found in the database!! Please register first. Hint: Make sure to pick your name from the list !!")
                 return render(request, 'insert_record.html')
        
        elif ( request.GET.get('currentweek') and request.GET.get('systemcode1') == '' and  request.GET.get('systemcode2') == '' and  request.GET.get('systemcode3') == '' and  request.GET.get('systemcode4') == ''  and  request.GET.get('systemcode5') == '' and  request.GET.get('systemcode6') == ''):
           if(request.GET.get('empname') and request.GET.get('department') and request.GET.get('currentweek')):
                 thisname = request.GET.get('empname')
                 new_week = int(request.GET.get('currentweek'))
                 objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [thisname])
                 six_days = []
                 year = date.today().year
                 six_days = [datetime.datetime.strptime(str(year) + "-W"+ str(new_week) + str(x), "%Y-W%W-%w").strftime('%d/%m/%Y') for x in range(-6,0)]

                 first_day = six_days[5]
                 second_day = six_days[4]
                 third_day = six_days[3]
                 fourth_day = six_days[2]
                 fifth_day = six_days[1]
                 sixth_day = six_days[0]
                 return render(request, 'insert_record.html', {"name": thisname, "data": objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": new_week})
           else:
                thisname = request.GET.get('empname')
                objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [thisname])
                now = datetime.datetime.now()
                today = (now.strftime("%A"))
                week = datetime.datetime.now().isocalendar()[1]
                if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None
                messages.success(request, "Submit your name first.")
                return render(request, 'insert_record.html', {"name": thisname, "data": objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})


                 
       
        elif request.GET.get('empname') and request.GET.get('department') and request.GET.get('currentweek')  and (request.GET.get('add1')  or request.GET.get('add2') or request.GET.get('add3')  or request.GET.get('add4')  or request.GET.get('add5')  or request.GET.get('add6') or request.GET.get('add7')  ):
                 flag = 0
                 empname = request.GET.get('empname')
                 thisweek = request.GET.get('currentweek')
                 new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
                 day1_syscode = timeTracking.objects.raw('SELECT id, systemcode1 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
                 day2_syscode = timeTracking.objects.raw('SELECT id, systemcode2 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
                 day3_syscode = timeTracking.objects.raw('SELECT id, systemcode3 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
                 day4_syscode = timeTracking.objects.raw('SELECT id, systemcode4 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
                 day5_syscode = timeTracking.objects.raw('SELECT id, systemcode5 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
                 day6_syscode = timeTracking.objects.raw('SELECT id, systemcode6 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
                 s1 =[]
                 s2 =[]
                 s3 = []
                 s4 = []
                 s5 = []
                 s6 = []
                 for sys1 in day1_syscode:
                     if (sys1 != None):
                         s1.append(sys1.systemcode1)
                 for sys2 in day2_syscode:
                     if (sys2 != None):
                         s2.append(sys2.systemcode2)
                 for sys3 in day3_syscode:
                     if (sys3 != None):
                         s3.append(sys3.systemcode3)
                 for sys4 in day4_syscode:
                     if (sys4 != None):
                         s4.append(sys4.systemcode4)
                 for sys5 in day5_syscode:
                     if (sys5 != None):
                         s5.append(sys5.systemcode5)
                 for sys6 in day6_syscode:
                     if (sys6 != None):
                         s6.append(sys6.systemcode6)

                 s1 = list(set(s1))
                 s2 = list(set(s2))
                 s3 = list(set(s3))
                 s4 = list(set(s4))
                 s5 = list(set(s5))
                 s6 = list(set(s6))
                 
                 tw1 = timeTracking.objects.raw( 'SELECT id, time_worked1 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
                 tw2 = timeTracking.objects.raw( 'SELECT id, time_worked2 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
                 tw3 = timeTracking.objects.raw( 'SELECT id, time_worked3 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
                 tw4 = timeTracking.objects.raw( 'SELECT id, time_worked4 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
                 tw5 = timeTracking.objects.raw( 'SELECT id, time_worked5 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])
                 tw6 = timeTracking.objects.raw( 'SELECT id, time_worked6 FROM time_history WHERE empname = %s and currentweek = %s ', [empname, thisweek])

                 Total_tw1 = 0
                 Total_tw2 = 0
                 Total_tw3 = 0
                 Total_tw4 = 0
                 Total_tw5 = 0
                 Total_tw6 = 0
                 for t in tw1:
                    if (t.time_worked1 != None):
                        Total_tw1 = t.time_worked1 + Total_tw1
                 for t in tw2:
                    if (t.time_worked2 != None):
                        Total_tw2 = t.time_worked2 + Total_tw2
                 for t in tw3:
                    if (t.time_worked3 != None):
                        Total_tw3 = t.time_worked3 + Total_tw3
                 for t in tw4:
                    if (t.time_worked4 != None):
                        Total_tw4 = t.time_worked4 + Total_tw4
                 for t in tw5:
                    if (t.time_worked5 != None):
                        Total_tw5 = t.time_worked5 + Total_tw5
                 for t in tw6:
                    if (t.time_worked6 != None):
                        Total_tw6 = t.time_worked6 + Total_tw6

                 
                 saverecord = timeTracking()
                 saverecord.empname = request.GET.get('empname')
                 saverecord.department = request.GET.get('department')
                 saverecord.currentweek = request.GET.get('currentweek')


                 if(request.GET.get('add1') and request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1')  and (request.GET.get('development_phase1') == '' or request.GET.get('development_phase1') in d_phases ) and (request.GET.get('project1') == '' or request.GET.get('project1') in projects ) and (request.GET.get('systemcode1') not in s1) and not (request.GET.get('systemcode1') not in lists ) and ((int (request.GET.get('time_worked1')) + Total_tw1) <= 10)):
                    d1 = request.GET.get('day1')
                    saverecord.day1 = datetime.datetime.strptime(d1, "%d/%m/%Y").date()
                    saverecord.systemcode1 = request.GET.get('systemcode1')
                    saverecord.time_worked1 = request.GET.get('time_worked1')
                    saverecord.development_phase1 = request.GET.get('development_phase1')
                    saverecord.project1 = request.GET.get('project1')
                 

                 elif(request.GET.get('add2') and request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')  and (request.GET.get('development_phase2') == '' or request.GET.get('development_phase2') in d_phases ) and (request.GET.get('project2') == '' or request.GET.get('project2') in projects )  and (request.GET.get('systemcode2') not in s2) and not (request.GET.get('systemcode2') not in lists ) and ((int (request.GET.get('time_worked2')) + Total_tw2) <= 10) ):
                    d2 = request.GET.get('day2')
                    saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                    saverecord.systemcode2 = request.GET.get('systemcode2')
                    saverecord.time_worked2 = request.GET.get('time_worked2')
                    saverecord.development_phase2 = request.GET.get('development_phase2')
                    saverecord.project2 = request.GET.get('project2')
                 

                 elif(request.GET.get('add3') and request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3')  and (request.GET.get('development_phase3') == '' or request.GET.get('development_phase3') in d_phases ) and (request.GET.get('project3') == '' or request.GET.get('project3') in projects ) and (request.GET.get('systemcode3') not in s3) and not (request.GET.get('systemcode3') not in lists )  and ((int (request.GET.get('time_worked3')) + Total_tw3) <= 10)):
                     d3 = request.GET.get('day3')
                     saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                     saverecord.time_worked3 = request.GET.get('time_worked3')
                     saverecord.systemcode3 = request.GET.get('systemcode3')
                     saverecord.development_phase3 = request.GET.get('development_phase3')
                     saverecord.project3 = request.GET.get('project3')
                    

                 elif(request.GET.get('add4') and request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')  and (request.GET.get('development_phase4') == '' or request.GET.get('development_phase4') in d_phases ) and (request.GET.get('project4') == '' or request.GET.get('project4') in projects ) and (request.GET.get('systemcode4') not in s4) and not (request.GET.get('systemcode4') not in lists ) and ((int (request.GET.get('time_worked4')) + Total_tw4) <= 10) ):
                     d4 = request.GET.get('day4')
                     saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                     saverecord.time_worked4 = request.GET.get('time_worked4')
                     saverecord.systemcode4 = request.GET.get('systemcode4')
                     saverecord.development_phase4 = request.GET.get('development_phase4')
                     saverecord.project4 = request.GET.get('project4')
                      

                 elif(request.GET.get('add5') and request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5')  and (request.GET.get('development_phase5') == '' or request.GET.get('development_phase5') in d_phases ) and (request.GET.get('project5') == '' or request.GET.get('project5') in projects ) and (request.GET.get('systemcode5') not in s5) and not (request.GET.get('systemcode5') not in lists ) and ((int (request.GET.get('time_worked5')) + Total_tw5) <= 10)):
                     d5 = request.GET.get('day5')
                     saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                     saverecord.time_worked5 = request.GET.get('time_worked5')
                     saverecord.systemcode5 = request.GET.get('systemcode5')
                     saverecord.development_phase5 = request.GET.get('development_phase5')
                     saverecord.project5 = request.GET.get('project5')

                 elif(request.GET.get('add6') and request.GET.get('day6') and request.GET.get('systemcode6') and request.GET.get('time_worked6')  and (request.GET.get('development_phase6') == '' or request.GET.get('development_phase6') in d_phases ) and (request.GET.get('project6') == '' or request.GET.get('project6') in projects ) and (request.GET.get('systemcode6') not in s6) and not (request.GET.get('systemcode6') not in lists ) and ((int (request.GET.get('time_worked6')) + Total_tw6) <= 10) ):
                     d6 = request.GET.get('day6')
                     saverecord.day6 = datetime.datetime.strptime(d6, "%d/%m/%Y").date()
                     saverecord.time_worked6 = request.GET.get('time_worked6')
                     saverecord.systemcode6 = request.GET.get('systemcode6')
                     saverecord.development_phase6 = request.GET.get('development_phase6')
                     saverecord.project6 = request.GET.get('project6')
                 

                 else:
                     saverecord.day1 = None
                     saverecord.time_worked1 = None
                     saverecord.development_phase1 = None
                     saverecord.project1 = None

                     saverecord.day2 = None
                     saverecord.time_worked2 = 0
                     saverecord.development_phase2 = None
                     saverecord.project2 = None

                     saverecord.day3 = None
                     saverecord.time_worked3 = None
                     saverecord.development_phase3 = None
                     saverecord.project3 = None

                     saverecord.day4 = None
                     saverecord.time_worked4 = None
                     saverecord.development_phase4 = None
                     saverecord.project4 = None

                     saverecord.day5 = None
                     saverecord.time_worked5 = None
                     saverecord.development_phase5 = None
                     saverecord.project5 = None


                     saverecord.day6 = None
                     saverecord.time_worked6 = None
                     saverecord.development_phase6 = None
                     saverecord.project6 = None
                     

                     saverecord.systemcode1 = None
                     saverecord.systemcode2 = None
                     saverecord.systemcode3 = None
                     saverecord.systemcode4 = None
                     saverecord.systemcode5 = None


                     now = datetime.datetime.now()
                     today = (now.strftime("%A"))
                     week = datetime.datetime.now().isocalendar()[1]
                     if (today == "Monday"):
                        first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                     elif (today == "Tuesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                     elif (today == "Wednesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                     elif (today == "Thursday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                     elif (today == "Friday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                     elif (today == "Saturday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                     else:

                        first_day = None
                        second_day = None
                        third_day = None
                        fourth_day = None
                        fifth_day = None
                        sixth_day = None


                     if ( request.GET.get('time_worked1') != '' and ((int(request.GET.get('time_worked1')) + Total_tw1) >= 10)) or (  request.GET.get('time_worked2') != ''  and ((int(request.GET.get('time_worked2')) + Total_tw2) >= 10)) or ( request.GET.get('time_worked3') != '' and ((int (request.GET.get('time_worked3')) + Total_tw3) >= 10)) or (  request.GET.get('time_worked4') != '' and ((int (request.GET.get('time_worked4')) + Total_tw4) >= 10)) or (request.GET.get('time_worked5') != '' and ((int (request.GET.get('time_worked5')) + Total_tw5) >= 10)) or ( request.GET.get('time_worked6') != ''  and ((int (request.GET.get('time_worked6')) + Total_tw6) >= 10)):
                        messages.success(request, "You cannot work for more than 10 hours on a certain day. Please go home :) ")
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})
                     
                     elif ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):
                        messages.success(request, "Error: Invalid system code or perhaps the system code for this day already exists or Invalid Development phase . Hint: Make sure to select Development Phase, Project and System Code from the list. ")
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})
                     else:
                        messages.success(request, "One or some of the dates modified, doesn't match with the current week !!")
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})

                    
                 now = datetime.datetime.now()
                 today = (now.strftime("%A"))
                 week = datetime.datetime.now().isocalendar()[1]
                 if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                 elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                 elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                 elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                 elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                 elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                 else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None

                 if ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):
                    saverecord.save()
                    messages.success(request, "Data saved successfully !!")
                    return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week":week })
                   
                 else:
                    messages.success(request, "One or some of the dates modified, doesn't match with the current week!!")
                    new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                    return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week":week })


                 
                 

        elif request.GET.get('empname') and request.GET.get('department') and request.GET.get('currentweek') and request.GET.get('send') :
          
                 
          if ((request.GET.get('systemcode1') != '' and request.GET.get('systemcode1') not in lists) or ( request.GET.get('systemcode2') != '' and request.GET.get('systemcode2') not in lists) or  ( request.GET.get('systemcode3') != '' and request.GET.get('systemcode3') not in lists) or ( request.GET.get('systemcode4') != '' and request.GET.get('systemcode4') not in lists) or ( request.GET.get('systemcode5') != '' and request.GET.get('systemcode5') not in lists) or ( request.GET.get('systemcode6') != '' and request.GET.get('systemcode6') not in lists)):


            now = datetime.datetime.now()
            today = (now.strftime("%A"))
            week = datetime.datetime.now().isocalendar()[1]
            if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

            elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

            elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

            elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
            elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

            elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
            else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None



            empname = request.GET.get('empname')
            messages.success(request, "Invalid system code, Please select one from the list!!")
            new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
           
            return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week":week })    
          
          elif ((request.GET.get('development_phase1') != '' and request.GET.get('development_phase1') not in d_phases ) or (request.GET.get('project1') != '' and  request.GET.get('project1') not in projects )) or  ((request.GET.get('development_phase2') != '' and request.GET.get('development_phase2') not in d_phases ) or (request.GET.get('project2') != '' and  request.GET.get('project2') not in projects )) or ((request.GET.get('development_phase3') != '' and request.GET.get('development_phase3') not in d_phases ) or (request.GET.get('project3') != '' and  request.GET.get('project3') not in projects )) or ((request.GET.get('development_phase4') != '' and request.GET.get('development_phase4') not in d_phases ) or (request.GET.get('project4') != '' and  request.GET.get('project4') not in projects )) or ((request.GET.get('development_phase5') != '' and request.GET.get('development_phase5') not in d_phases ) or (request.GET.get('project5') != '' and  request.GET.get('project5') not in projects )) or ((request.GET.get('development_phase6') != '' and request.GET.get('development_phase6') not in d_phases ) or (request.GET.get('project6') != '' and  request.GET.get('project6') not in projects )):
              
            now = datetime.datetime.now()
            today = (now.strftime("%A"))
            week = datetime.datetime.now().isocalendar()[1]
            if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

            elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

            elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

            elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
            elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

            elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
            else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None



            empname = request.GET.get('empname')
            messages.success(request, "Invalid Development phase or Project!! Please leave them null or select from the list. ")
            new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
           
            return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week":week })


          elif ( request.GET.get('time_worked1') != '' and ((int(request.GET.get('time_worked1')) + Total_tw1) >= 10)) or (  request.GET.get('time_worked2') != ''  and ((int(request.GET.get('time_worked2')) + Total_tw2) >= 10)) or ( request.GET.get('time_worked3') != '' and ((int (request.GET.get('time_worked3')) + Total_tw3) >= 10)) or (  request.GET.get('time_worked4') != '' and ((int (request.GET.get('time_worked4')) + Total_tw4) >= 10)) or (request.GET.get('time_worked5') != '' and ((int (request.GET.get('time_worked5')) + Total_tw5) >= 10)) or ( request.GET.get('time_worked6') != ''  and ((int (request.GET.get('time_worked6')) + Total_tw6) >= 10)):
            now = datetime.datetime.now()
            today = (now.strftime("%A"))
            week = datetime.datetime.now().isocalendar()[1]
            if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

            elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

            elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

            elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
            elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

            elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
            else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None



            empname = request.GET.get('empname')
            messages.success(request, "You cannot work for more than 10 hours on a certain day. Please go home :) ")
            new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
           
            return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week":week })
                    
          
          else: 
            
            empname = request.GET.get('empname')
            new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])


            thisweek = request.GET.get('currentweek')
            new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
            day1_syscode = timeTracking.objects.raw('SELECT id, systemcode1 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
            day2_syscode = timeTracking.objects.raw('SELECT id, systemcode2 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
            day3_syscode = timeTracking.objects.raw('SELECT id, systemcode3 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
            day4_syscode = timeTracking.objects.raw('SELECT id, systemcode4 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
            day5_syscode = timeTracking.objects.raw('SELECT id, systemcode5 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
            day6_syscode = timeTracking.objects.raw('SELECT id, systemcode6 FROM time_history WHERE empname = %s and currentweek = %s', [empname, thisweek])
            s1 =[]
            s2 =[]
            s3 = []
            s4 = []
            s5 = []
            s6 = []
            for sys1 in day1_syscode:
                if (sys1 != None):
                    s1.append(sys1.systemcode1)
            for sys2 in day2_syscode:
                if (sys2 != None):
                    s2.append(sys2.systemcode2)
            for sys3 in day3_syscode:
                if (sys3 != None):
                    s3.append(sys3.systemcode3)
            for sys4 in day4_syscode:
                if (sys4 != None):
                    s4.append(sys4.systemcode4)
            for sys5 in day5_syscode:
                if (sys5 != None):
                    s5.append(sys5.systemcode5)
            for sys6 in day6_syscode:
                if (sys6 != None):
                    s6.append(sys6.systemcode6)

            s1 = list(set(s1))
            s2 = list(set(s2))
            s3 = list(set(s3))
            s4 = list(set(s4))
            s5 = list(set(s5))
            s6 = list(set(s6))


              
                 
            saverecord = timeTracking()
            saverecord.empname = request.GET.get('empname')
            saverecord.department = request.GET.get('department')
            saverecord.currentweek = request.GET.get('currentweek')
                 
           
            if (request.GET.get('systemcode1') == request.GET.get('systemcode2') and request.GET.get('development_phase1') != request.GET.get('development_phase2')) or (request.GET.get('systemcode1') == request.GET.get('systemcode3') and request.GET.get('development_phase1') != request.GET.get('development_phase3'))  or (request.GET.get('systemcode1') == request.GET.get('systemcode4') and request.GET.get('development_phase1') != request.GET.get('development_phase4')) or (request.GET.get('systemcode1') == request.GET.get('systemcode5') and request.GET.get('development_phase1') != request.GET.get('development_phase5'))  or (request.GET.get('systemcode1') == request.GET.get('systemcode6') and request.GET.get('development_phase1') != request.GET.get('development_phase6')): 
                     week = datetime.datetime.now().isocalendar()[1]
                     now = datetime.datetime.now()
                     today = (now.strftime("%A"))
                     if (today == "Monday"):
                        first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                     elif (today == "Tuesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                     elif (today == "Wednesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                     elif (today == "Thursday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                     elif (today == "Friday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                     elif (today == "Saturday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                     else:

                        first_day = None
                        second_day = None
                        third_day = None
                        fourth_day = None
                        fifth_day = None
                        sixth_day = None


                     if ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):

                        messages.success(request, "Please fill the system codes with same development phase or use the + option to enter individual records...")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week })
                     else:
                        messages.success(request, "One or some of the dates modified, doesn't match with the current week !!")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})

            elif   (request.GET.get('systemcode2') == request.GET.get('systemcode3') and request.GET.get('development_phase2') != request.GET.get('development_phase3'))  or (request.GET.get('systemcode2') == request.GET.get('systemcode4') and request.GET.get('development_phase2') != request.GET.get('development_phase4')) or (request.GET.get('systemcode2') == request.GET.get('systemcode5') and request.GET.get('development_phase2') != request.GET.get('development_phase5'))  or (request.GET.get('systemcode2') == request.GET.get('systemcode6') and request.GET.get('development_phase2') != request.GET.get('development_phase6')):

                     week = datetime.datetime.now().isocalendar()[1]
                     now = datetime.datetime.now()
                     today = (now.strftime("%A"))
                     if (today == "Monday"):
                        first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                     elif (today == "Tuesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                     elif (today == "Wednesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                     elif (today == "Thursday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                     elif (today == "Friday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                     elif (today == "Saturday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                     else:

                        first_day = None
                        second_day = None
                        third_day = None
                        fourth_day = None
                        fifth_day = None
                        sixth_day = None


                     if ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):

                        messages.success(request, " To use the SEND button, Please fill the system codes with same development phase or use the + buttons to enter individual records...")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week })
                     else:
                        messages.success(request, "One or some of the dates modified, doesn't match with the current week !!")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})
            elif   (request.GET.get('systemcode3') == request.GET.get('systemcode4') and request.GET.get('development_phase3') != request.GET.get('development_phase4')) or (request.GET.get('systemcode3') == request.GET.get('systemcode5') and request.GET.get('development_phase3') != request.GET.get('development_phase5'))  or (request.GET.get('systemcode3') == request.GET.get('systemcode6') and request.GET.get('development_phase3') != request.GET.get('development_phase6')):

                     week = datetime.datetime.now().isocalendar()[1]
                     now = datetime.datetime.now()
                     today = (now.strftime("%A"))
                     if (today == "Monday"):
                        first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                     elif (today == "Tuesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                     elif (today == "Wednesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                     elif (today == "Thursday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                     elif (today == "Friday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                     elif (today == "Saturday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                     else:

                        first_day = None
                        second_day = None
                        third_day = None
                        fourth_day = None
                        fifth_day = None
                        sixth_day = None


                     if ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):

                        messages.success(request, " To use the SEND button, Please fill the system codes with same development phase or use the + buttons to enter individual records...")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week })
                     else:
                        messages.success(request, "One or some of the dates modified, doesn't match with the current week !!")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})

            elif  (request.GET.get('systemcode4') == request.GET.get('systemcode5') and request.GET.get('development_phase4') != request.GET.get('development_phase5'))  or (request.GET.get('systemcode4') == request.GET.get('systemcode6') and request.GET.get('development_phase4') != request.GET.get('development_phase6')):

                     week = datetime.datetime.now().isocalendar()[1]
                     now = datetime.datetime.now()
                     today = (now.strftime("%A"))
                     if (today == "Monday"):
                        first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                     elif (today == "Tuesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                     elif (today == "Wednesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                     elif (today == "Thursday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                     elif (today == "Friday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                     elif (today == "Saturday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                     else:

                        first_day = None
                        second_day = None
                        third_day = None
                        fourth_day = None
                        fifth_day = None
                        sixth_day = None


                     if ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):

                        messages.success(request, " To use the SEND button, Please fill the system codes with same development phase or use the + buttons to enter individual records...")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week })
                     else:
                        messages.success(request, "One or some of the dates modified, doesn't match with the current week !!")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})

            elif  (request.GET.get('systemcode5') == request.GET.get('systemcode6') and request.GET.get('development_phase5') != request.GET.get('development_phase6')):

                     week = datetime.datetime.now().isocalendar()[1]
                     now = datetime.datetime.now()
                     today = (now.strftime("%A"))
                     if (today == "Monday"):
                        first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                     elif (today == "Tuesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                     elif (today == "Wednesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                     elif (today == "Thursday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                     elif (today == "Friday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                     elif (today == "Saturday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                     else:

                        first_day = None
                        second_day = None
                        third_day = None
                        fourth_day = None
                        fifth_day = None
                        sixth_day = None


                     if ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):

                        messages.success(request, " To use the SEND button, Please fill the system codes with same development phase or use the + buttons to enter individual records...")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week })
                     else:
                        messages.success(request, "One or some of the dates modified, doesn't match with the current week !!")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})

      










            elif request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1')  and  (request.GET.get('systemcode1') not in s1 and not request.GET.get('systemcode2')):
                d1 = request.GET.get('day1')
                saverecord.day1 = datetime.datetime.strptime(d1, "%d/%m/%Y").date()
                saverecord.systemcode1 = request.GET.get('systemcode1')
                saverecord.time_worked1 = request.GET.get('time_worked1')
                saverecord.development_phase1 = request.GET.get('development_phase1')
                saverecord.project1 = request.GET.get('project1')
            elif ((request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and not request.GET.get('systemcode3') and (request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1'))  and  request.GET.get('systemcode1') not in s1 and  request.GET.get('systemcode2') not in s2 and not request.GET.get('systemcode3')  ):
                d1 = request.GET.get('day1')
                saverecord.day1 = datetime.datetime.strptime(d1, "%d/%m/%Y").date()
                saverecord.systemcode1 = request.GET.get('systemcode1')
                saverecord.time_worked1 = request.GET.get('time_worked1')
                saverecord.development_phase1 = request.GET.get('development_phase1')
                saverecord.project1 = request.GET.get('project1')

                d2 = request.GET.get('day2')
                saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                saverecord.systemcode2 = request.GET.get('systemcode2')
                saverecord.time_worked2 = request.GET.get('time_worked2')
                saverecord.development_phase2 = request.GET.get('development_phase2')
                saverecord.project2 = request.GET.get('project2')
                    
               
                
            
            elif ((request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3'))  and (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and (request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1'))  and  request.GET.get('systemcode1') not in s1 and  request.GET.get('systemcode2') not in s2 and  request.GET.get('systemcode3') not in s3  and not request.GET.get('systemcode4') ):
                
                
                d1 = request.GET.get('day1')
                saverecord.day1 = datetime.datetime.strptime(d1, "%d/%m/%Y").date()
                saverecord.systemcode1 = request.GET.get('systemcode1')
                saverecord.time_worked1 = request.GET.get('time_worked1')
                saverecord.development_phase1 = request.GET.get('development_phase1')
                saverecord.project1 = request.GET.get('project1')

                d2 = request.GET.get('day2')
                saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                saverecord.systemcode2 = request.GET.get('systemcode2')
                saverecord.time_worked2 = request.GET.get('time_worked2')
                saverecord.development_phase2 = request.GET.get('development_phase2')
                saverecord.project2 = request.GET.get('project2')

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')
                

            elif ( (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3')) and (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and (request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1')) and  request.GET.get('systemcode1') not in s1 and  request.GET.get('systemcode2') not in s2 and  request.GET.get('systemcode3') not in s3 and  request.GET.get('systemcode4') not in s4  and not request.GET.get('systemcode5')):
                
                
                d1 = request.GET.get('day1')
                saverecord.day1 = datetime.datetime.strptime(d1, "%d/%m/%Y").date()
                saverecord.systemcode1 = request.GET.get('systemcode1')
                saverecord.time_worked1 = request.GET.get('time_worked1')
                saverecord.development_phase1 = request.GET.get('development_phase1')
                saverecord.project1 = request.GET.get('project1')

                d2 = request.GET.get('day2')
                saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                saverecord.systemcode2 = request.GET.get('systemcode2')
                saverecord.time_worked2 = request.GET.get('time_worked2')
                saverecord.development_phase2 = request.GET.get('development_phase2')
                saverecord.project2 = request.GET.get('project2')

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')
               

            elif ( (request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5')) and (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3')) and (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and (request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1')) and not (request.GET.get('day6') and request.GET.get('systemcode6') and request.GET.get('time_worked6')) and  request.GET.get('systemcode1') not in s1 and  request.GET.get('systemcode2') not in s2 and  request.GET.get('systemcode3') not in s3 and  request.GET.get('systemcode4') not in s4 and  request.GET.get('systemcode5') not in s5  and not request.GET.get('systemcode6')) :
                
                
                d1 = request.GET.get('day1')
                saverecord.day1 = datetime.datetime.strptime(d1, "%d/%m/%Y").date()
                saverecord.systemcode1 = request.GET.get('systemcode1')
                saverecord.time_worked1 = request.GET.get('time_worked1')
                saverecord.development_phase1 = request.GET.get('development_phase1')
                saverecord.project1 = request.GET.get('project1')

                d2 = request.GET.get('day2')
                saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                saverecord.systemcode2 = request.GET.get('systemcode2')
                saverecord.time_worked2 = request.GET.get('time_worked2')
                saverecord.development_phase2 = request.GET.get('development_phase2')
                saverecord.project2 = request.GET.get('project2')

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

                d5 = request.GET.get('day5')
                saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                saverecord.systemcode5 = request.GET.get('systemcode5')
                saverecord.time_worked5 = request.GET.get('time_worked5')
                saverecord.development_phase5 = request.GET.get('development_phase5')
                saverecord.project5 = request.GET.get('project5')



               

            elif  ((request.GET.get('day6') and request.GET.get('systemcode6') and request.GET.get('time_worked6')) and (request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5')) and (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3')) and (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and (request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1')) and  request.GET.get('systemcode1') not in s1 and  request.GET.get('systemcode2') not in s2 and  request.GET.get('systemcode3') not in s3 and  request.GET.get('systemcode4') not in s4 and  request.GET.get('systemcode5') not in s5 and  request.GET.get('systemcode6') not in s6 ):
                
                
                d1 = request.GET.get('day1')
                saverecord.day1 = datetime.datetime.strptime(d1, "%d/%m/%Y").date()
                saverecord.systemcode1 = request.GET.get('systemcode1')
                saverecord.time_worked1 = request.GET.get('time_worked1')
                saverecord.development_phase1 = request.GET.get('development_phase1')
                saverecord.project1 = request.GET.get('project1')

                d2 = request.GET.get('day2')
                saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                saverecord.systemcode2 = request.GET.get('systemcode2')
                saverecord.time_worked2 = request.GET.get('time_worked2')
                saverecord.development_phase2 = request.GET.get('development_phase2')
                saverecord.project2 = request.GET.get('project2')

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

                d5 = request.GET.get('day5')
                saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                saverecord.systemcode5 = request.GET.get('systemcode5')
                saverecord.time_worked5 = request.GET.get('time_worked5')
                saverecord.development_phase5 = request.GET.get('development_phase5')
                saverecord.project5 = request.GET.get('project5')

                d6 = request.GET.get('day6')
                saverecord.day6 = datetime.datetime.strptime(d6, "%d/%m/%Y").date()
                saverecord.systemcode6 = request.GET.get('systemcode6')
                saverecord.time_worked6 = request.GET.get('time_worked6')
                saverecord.development_phase6 = request.GET.get('development_phase6')
                saverecord.project6 = request.GET.get('project6')






            elif ((request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3'))  and (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and not (request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1'))  and  request.GET.get('systemcode2') not in s2 and  request.GET.get('systemcode3') not in s3 and not request.GET.get('systemcode4') ):

                d2 = request.GET.get('day2')
                saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                saverecord.systemcode2 = request.GET.get('systemcode2')
                saverecord.time_worked2 = request.GET.get('time_worked2')
                saverecord.development_phase2 = request.GET.get('development_phase2')
                saverecord.project2 = request.GET.get('project2')

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

            elif ((request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3'))  and (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and not (request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1'))  and  request.GET.get('systemcode2') not in s2 and  request.GET.get('systemcode3') not in s3 and request.GET.get('systemcode4') not in s4 and not request.GET.get('systemcode5') ):

                d2 = request.GET.get('day2')
                saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                saverecord.systemcode2 = request.GET.get('systemcode2')
                saverecord.time_worked2 = request.GET.get('time_worked2')
                saverecord.development_phase2 = request.GET.get('development_phase2')
                saverecord.project2 = request.GET.get('project2')

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

            elif ((request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5'))  and (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3'))  and (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and not (request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1'))  and  request.GET.get('systemcode2') not in s2 and  request.GET.get('systemcode3') not in s3 and request.GET.get('systemcode4') not in s4  and request.GET.get('systemcode5') not in s5  and not request.GET.get('systemcode6') ):

                d2 = request.GET.get('day2')
                saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                saverecord.systemcode2 = request.GET.get('systemcode2')
                saverecord.time_worked2 = request.GET.get('time_worked2')
                saverecord.development_phase2 = request.GET.get('development_phase2')
                saverecord.project2 = request.GET.get('project2')

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

                d5 = request.GET.get('day5')
                saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                saverecord.systemcode5 = request.GET.get('systemcode5')
                saverecord.time_worked5 = request.GET.get('time_worked5')
                saverecord.development_phase5 = request.GET.get('development_phase5')
                saverecord.project5 = request.GET.get('project5')

            elif ((request.GET.get('day6') and request.GET.get('systemcode6') and request.GET.get('time_worked6')) and (request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5'))  and (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3'))  and (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and not (request.GET.get('day1') and request.GET.get('systemcode1') and request.GET.get('time_worked1'))  and  request.GET.get('systemcode2') not in s2 and  request.GET.get('systemcode3') not in s3 and request.GET.get('systemcode4') not in s4  and request.GET.get('systemcode5') not in s5  and request.GET.get('systemcode6') not in s6):

                d2 = request.GET.get('day2')
                saverecord.day2 = datetime.datetime.strptime(d2, "%d/%m/%Y").date()
                saverecord.systemcode2 = request.GET.get('systemcode2')
                saverecord.time_worked2 = request.GET.get('time_worked2')
                saverecord.development_phase2 = request.GET.get('development_phase2')
                saverecord.project2 = request.GET.get('project2')

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

                d5 = request.GET.get('day5')
                saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                saverecord.systemcode5 = request.GET.get('systemcode5')
                saverecord.time_worked5 = request.GET.get('time_worked5')
                saverecord.development_phase5 = request.GET.get('development_phase5')
                saverecord.project5 = request.GET.get('project5')

                d6 = request.GET.get('day6')
                saverecord.day6 = datetime.datetime.strptime(d6, "%d/%m/%Y").date()
                saverecord.systemcode6 = request.GET.get('systemcode6')
                saverecord.time_worked6 = request.GET.get('time_worked6')
                saverecord.development_phase6 = request.GET.get('development_phase6')
                saverecord.project6 = request.GET.get('project6')





            elif ((request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3')) and not (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2')) and request.GET.get('systemcode3') not in s3 and request.GET.get('systemcode4') not in s4  ):

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

            elif ((request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5'))  and (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3'))  and not (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2'))  and  request.GET.get('systemcode3') not in s3 and request.GET.get('systemcode4') not in s4  and request.GET.get('systemcode5') not in s5 ):

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

                d5 = request.GET.get('day5')
                saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                saverecord.systemcode5 = request.GET.get('systemcode5')
                saverecord.time_worked5 = request.GET.get('time_worked5')
                saverecord.development_phase5 = request.GET.get('development_phase5')
                saverecord.project5 = request.GET.get('project5')

            elif ((request.GET.get('day6') and request.GET.get('systemcode6') and request.GET.get('time_worked6')) and (request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5'))  and (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3'))  and not (request.GET.get('day2') and request.GET.get('systemcode2') and request.GET.get('time_worked2'))  and  request.GET.get('systemcode3') not in s3 and request.GET.get('systemcode4') not in s4  and request.GET.get('systemcode5') not in s5  and request.GET.get('systemcode6') not in s6 ):

                d3 = request.GET.get('day3')
                saverecord.day3 = datetime.datetime.strptime(d3, "%d/%m/%Y").date()
                saverecord.systemcode3 = request.GET.get('systemcode3')
                saverecord.time_worked3 = request.GET.get('time_worked3')
                saverecord.development_phase3 = request.GET.get('development_phase3')
                saverecord.project3 = request.GET.get('project3')

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

                d5 = request.GET.get('day5')
                saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                saverecord.systemcode5 = request.GET.get('systemcode5')
                saverecord.time_worked5 = request.GET.get('time_worked5')
                saverecord.development_phase5 = request.GET.get('development_phase5')
                saverecord.project5 = request.GET.get('project5')

                d6 = request.GET.get('day6')
                saverecord.day6 = datetime.datetime.strptime(d6, "%d/%m/%Y").date()
                saverecord.systemcode6 = request.GET.get('systemcode6')
                saverecord.time_worked6 = request.GET.get('time_worked6')
                saverecord.development_phase6 = request.GET.get('development_phase6')
                saverecord.project6 = request.GET.get('project6')




            elif ((request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5'))  and (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and not (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3')) and request.GET.get('systemcode4') not in s4  and request.GET.get('systemcode5') not in s5  and not request.GET.get('systemcode6') ):

                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

                d5 = request.GET.get('day5')
                saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                saverecord.systemcode5 = request.GET.get('systemcode5')
                saverecord.time_worked5 = request.GET.get('time_worked5')
                saverecord.development_phase5 = request.GET.get('development_phase5')
                saverecord.project5 = request.GET.get('project5')
            elif ((request.GET.get('day6') and request.GET.get('systemcode6') and request.GET.get('time_worked6')) and (request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5'))  and (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and not (request.GET.get('day3') and request.GET.get('systemcode3') and request.GET.get('time_worked3')) and request.GET.get('systemcode4') not in s4  and request.GET.get('systemcode5') not in s5  and request.GET.get('systemcode6') not in s6  ):


                d4 = request.GET.get('day4')
                saverecord.day4 = datetime.datetime.strptime(d4, "%d/%m/%Y").date()
                saverecord.systemcode4 = request.GET.get('systemcode4')
                saverecord.time_worked4 = request.GET.get('time_worked4')
                saverecord.development_phase4 = request.GET.get('development_phase4')
                saverecord.project4 = request.GET.get('project4')

                d5 = request.GET.get('day5')
                saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                saverecord.systemcode5 = request.GET.get('systemcode5')
                saverecord.time_worked5 = request.GET.get('time_worked5')
                saverecord.development_phase5 = request.GET.get('development_phase5')
                saverecord.project5 = request.GET.get('project5')

                d6 = request.GET.get('day6')
                saverecord.day6 = datetime.datetime.strptime(d6, "%d/%m/%Y").date()
                saverecord.systemcode6 = request.GET.get('systemcode6')
                saverecord.time_worked6 = request.GET.get('time_worked6')
                saverecord.development_phase6 = request.GET.get('development_phase6')
                saverecord.project6 = request.GET.get('project6')


            elif ((request.GET.get('day6') and request.GET.get('systemcode6') and request.GET.get('time_worked6')) and (request.GET.get('day5') and request.GET.get('systemcode5') and request.GET.get('time_worked5')) and not (request.GET.get('day4') and request.GET.get('systemcode4') and request.GET.get('time_worked4')) and request.GET.get('systemcode5') not in s5  and request.GET.get('systemcode6') not in s6  ):
                
                d5 = request.GET.get('day5')
                saverecord.day5 = datetime.datetime.strptime(d5, "%d/%m/%Y").date()
                saverecord.systemcode5 = request.GET.get('systemcode5')
                saverecord.time_worked5 = request.GET.get('time_worked5')
                saverecord.development_phase5 = request.GET.get('development_phase5')
                saverecord.project5 = request.GET.get('project5')

                d6 = request.GET.get('day6')
                saverecord.day6 = datetime.datetime.strptime(d6, "%d/%m/%Y").date()
                saverecord.systemcode6 = request.GET.get('systemcode6')
                saverecord.time_worked6 = request.GET.get('time_worked6')
                saverecord.development_phase6 = request.GET.get('development_phase6')
                saverecord.project6 = request.GET.get('project6')

               

            else:
                     saverecord.day1 = None
                     saverecord.time_worked1 = None
                     saverecord.development_phase1 = None
                     saverecord.project1 = None

                     saverecord.day2 = None
                     saverecord.time_worked2 = 0
                     saverecord.development_phase2 = None
                     saverecord.project2 = None

                     saverecord.day3 = None
                     saverecord.time_worked3 = None
                     saverecord.development_phase3 = None
                     saverecord.project3 = None

                     saverecord.day4 = None
                     saverecord.time_worked4 = None
                     saverecord.development_phase4 = None
                     saverecord.project4 = None

                     saverecord.day5 = None
                     saverecord.time_worked5 = None
                     saverecord.development_phase5 = None
                     saverecord.project5 = None


                     saverecord.day6 = None
                     saverecord.time_worked6 = None
                     saverecord.development_phase6 = None
                     saverecord.project6 = None
                     

                     saverecord.systemcode1 = None
                     saverecord.systemcode2 = None
                     saverecord.systemcode3 = None
                     saverecord.systemcode4 = None
                     saverecord.systemcode5 = None



                     week = datetime.datetime.now().isocalendar()[1]
                     now = datetime.datetime.now()
                     today = (now.strftime("%A"))
                     if (today == "Monday"):
                        first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

                     elif (today == "Tuesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

                     elif (today == "Wednesday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

                     elif (today == "Thursday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
                     elif (today == "Friday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                        sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

                     elif (today == "Saturday"):
                        first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                        second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                        third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                        fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                        fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                        sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
                     else:

                        first_day = None
                        second_day = None
                        third_day = None
                        fourth_day = None
                        fifth_day = None
                        sixth_day = None


                     if ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):

                        messages.success(request, "You are trying to use the Send button for a single record. Please use the + button")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week })
                     else:
                        messages.success(request, "One or some of the dates modified, doesn't match with the current week !!")
                        empname = request.GET.get('empname')
                        new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                        return render(request, 'insert_record.html', {"name": empname, "data": new_objects,"first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})

            week = datetime.datetime.now().isocalendar()[1]
            now = datetime.datetime.now()
            today = (now.strftime("%A"))
            if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

            elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

            elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

            elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
            elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

            elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
            else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None

            
            if ( int(request.GET.get('currentweek')) == week and request.GET.get('day1') == first_day  and request.GET.get('day2') == second_day and request.GET.get('day3') == third_day  and request.GET.get('day4') == fourth_day  and request.GET.get('day5') == fifth_day  and request.GET.get('day6') == sixth_day  ):
                saverecord.save()
                messages.success(request, "Data saved successfully !!")
                new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})
            else:
                messages.success(request, "One or some of the days modified, doesn't exist in the current week !!")
                new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
                return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})

        else:   
            week = datetime.datetime.now().isocalendar()[1]
            now = datetime.datetime.now()
            today = (now.strftime("%A"))
            if (today == "Monday"):
                    first_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=5)).strftime('%d/%m/%Y')

            elif (today == "Tuesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    second_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=4)).strftime('%d/%m/%Y')

            elif (today == "Wednesday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    third_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=3)).strftime('%d/%m/%Y')

            elif (today == "Thursday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fourth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                
            elif (today == "Friday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    fifth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                    sixth_day = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')

            elif (today == "Saturday"):
                    first_day = (datetime.datetime.today() - datetime.timedelta(days=5)).strftime('%d/%m/%Y')
                    second_day = (datetime.datetime.today() - datetime.timedelta(days=4)).strftime('%d/%m/%Y')
                    third_day = (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%d/%m/%Y')
                    fourth_day = (datetime.datetime.today() - datetime.timedelta(days=2)).strftime('%d/%m/%Y')
                    fifth_day = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%d/%m/%Y')
                    sixth_day = datetime.datetime.today().strftime('%d/%m/%Y')
                
            else:

                    first_day = None
                    second_day = None
                    third_day = None
                    fourth_day = None
                    fifth_day = None
                    sixth_day = None


               
            empname = request.GET.get('empname')
            new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
            return render(request, 'insert_record.html', {"name": empname, "data": new_objects, "first_day": first_day, "second_day": second_day, "third_day": third_day, "fourth_day":fourth_day, "fifth_day":fifth_day, "sixth_day":sixth_day, "week": week})




def display(request):
    if (request.method == 'POST'):
        
        if request.POST.get('empname') and request.POST.get('push'):
            thisname = request.POST.get('empname')
            objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [thisname])
            
            return render(request, 'display.html', {"name": thisname, "data": objects})


        elif request.POST.get('empname') and request.POST.get('dump'):
            thisname = request.POST.get('empname')
            thisweek = int(request.POST.get('currentweek'))
            objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])

            objects2 = timeTracking.objects.values()
            df = pd.DataFrame(list(objects2), columns = [ 'empname', 'department', 'currentweek', 'day1', 'time_worked1', 'systemcode1', 'development_phase1', 'project1', 'day2', 'time_worked2', 'systemcode2', 'development_phase2', 'project2', 'day3', 'time_worked3', 'systemcode3', 'development_phase3', 'project3', 'day4', 'time_worked4', 'systemcode4', 'development_phase4', 'project4', 'day5', 'time_worked5', 'systemcode5', 'development_phase5', 'project5', 'day6', 'time_worked6', 'systemcode6', 'development_phase6', 'project6'  ])
            df = df.loc[(df['empname'] == thisname) & (df['currentweek'] == thisweek)]
            
            df1 =  pd.DataFrame(columns = [ 'Name', 'Current Week', 'System Code', 'Department', 'Development Phase', 'Project', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
            df2 =  pd.DataFrame(columns = [ 'Name', 'Current Week', 'System Code', 'Department', 'Development Phase', 'Project', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
            df3 =  pd.DataFrame(columns = [ 'Name', 'Current Week', 'System Code', 'Department', 'Development Phase', 'Project', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

            df4 =  pd.DataFrame(columns = [ 'Name', 'Current Week', 'System Code', 'Department', 'Development Phase', 'Project', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
            df5 =  pd.DataFrame(columns = [ 'Name', 'Current Week', 'System Code', 'Department', 'Development Phase', 'Project', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
            df6 =  pd.DataFrame(columns = [ 'Name', 'Current Week', 'System Code', 'Department', 'Development Phase', 'Project', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
            df7 =  pd.DataFrame(columns = [ 'Name', 'Current Week', 'System Code', 'Department', 'Development Phase', 'Project', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

            

            df1['System Code'] = df['systemcode1']
            df1['Department'] =   df['department']
            df1['Development Phase'] = df['development_phase1']
            df1['Project'] = df['project1']
            df1['Monday'] = df['time_worked1']

            df2['System Code'] = df['systemcode2']
            df2['Department'] =   df['department']
            df2['Development Phase'] = df['development_phase2']
            df2['Project'] = df['project2']
            df2['Tuesday'] = df['time_worked2']
            df2 = df2[df2['System Code'].notna()]
            df1 = df1.append(df2)

            df3['System Code'] = df['systemcode3']
            df3['Department'] =   df['department']
            df3['Development Phase'] = df['development_phase3']
            df3['Project'] = df['project3']
            df3['Wednesday'] = df['time_worked3']
            df3 = df3[df3['System Code'].notna()]
            df1 = df1.append(df3)

            df4['System Code'] = df['systemcode4']
            df4['Department'] =   df['department']
            df4['Development Phase'] = df['development_phase4']
            df4['Project'] = df['project4']
            df4['Thursday'] = df['time_worked4']
            df4 = df4[df4['System Code'].notna()]
            df1 = df1.append(df4)

            df5['System Code'] = df['systemcode5']
            df5['Department'] =   df['department']
            df5['Development Phase'] = df['development_phase5']
            df5['Project'] = df['project5']
            df5['Friday'] = df['time_worked5']
            df5 = df5[df5['System Code'].notna()]
            df1 = df1.append(df5)

            df6['System Code'] = df['systemcode6']
            df6['Department'] =   df['department']
            df6['Development Phase'] = df['development_phase6']
            df6['Project'] = df['project6']
            df6['Saturday'] = df['time_worked6']
            df6 = df6[df6['System Code'].notna()]
            df1 = df1.append(df6)

            df1.loc['Total'] = df1.sum()
            df1= pd.DataFrame(df1)
           
            df8 = df1.loc['Total']
            df8 = df8['Monday': 'Saturday' ]
            length = len(df1)-1
            df1 = df1[1: length]
            df1 = df1.append(df8)
            
            for i in range(len(df1)-1):
                df1['Name'].iloc[i] = thisname 
                df1['Current Week'].iloc[i]= thisweek
            #df1 = df1.reset_index(inplace = True)
            
              
               


           

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="weekly_data2.xlsx"'                                        
            df1.to_excel(response)
            return response



        elif request.POST.get('empname') and request.POST.get('dump2'):
           name_lists = ['Tommaso_Capuano', 'Jonas_Weis', 'Kiran_Chincholi', 'Juan_R._Llobet', 'Shahid_Mobin', 'Matthias_Hecht', 'Marc_Haßenpflug', 'Lucian-Mircea_Grec', 'Isaac_Lopez', 'Rishabh_Yadav', 'Prathamesh_Malpathak', 'Julian_Erdle', 'Jakob_Habermann', 'Moritz_Baur', 'Gerhard_Becker', 'Fabian_Braun', 'Sebastian_Reiter', 'Dangelo_Aniello', 'Jacob_Lawson', 'Francesc_Betorz', 'Thorben_Schmitz ', 'Geoffroy_de_Dinechin', 'Rehan_Bandara', 'Emmanuel_Telmar', 'Jean_Labuschagne', 'Alberto_Progida ', 'Adrian_Lorenz', 'Robin_Scholtes', 'Julie_Letoile ', 'Mihir_Patwardhan', 'Jacopo_Irone', 'Stefan_Brieschenk', 'Maximilian_Pfohl', 'Johann_Gogesch', 'Tobias_Drexl', 'Thomas_Mason', 'Shrinivas_Iyengar ', 'Martin_Lee', 'Titto_Ephraim_Methew', 'Calvin_Füller', 'Oliver_Hitchens', 'Brunno_B._Vasques', 'Ramzi_Aouimeur', 'Jude_Sudario', 'Giulio_Pacifici', 'Kilian_Reutter', 'Ilker_Yasar', 'Robin_Duhnsen', 'Victor_Covasan', 'Sven_Deist', 'Jannis_Bobinger', 'Jaime_Aguirre', 'Alan_Rochford', 'Matthias_Jacoby', 'Dragos_Varsescu', 'Mathieu_Rayer', 'Elia_Poli', 'Christophe_Geuens', 'Samuel_Leitenmeier ', 'Anton_Liegert', 'Stefan_Eisenknappl', 'Maximilian_Koch', 'Veronika_Pröller', 'Tomasz_Witkowski', 'Omar_Abrahams', 'Emily_Seeberg', 'Fabio_Kerstens', 'Nian_Fuls', 'Patrick_Wagner', 'Marius_Hahn', 'Ines_Pereirinha', 'Andreas_Stark', 'Dmitrii_Matias', 'Filipe_Valentim', 'Amir_Ibrahim', 'Lukas_Welzel', 'Stephan_Schmid', 'David_Maiden ', 'Vasyl_Kashevko', 'Nadine_Steck', 'Laura_Soldo', 'Mario_Araujo', 'Jyotiben_Tiwari', 'Pierre_Groslambert', 'Michael_Mair', 'Jörn_Spurmann', 'Nicholas_Tegg', 'Rolf_Wubben', 'Almero_Gerber', 'Kevin_Eppenga', 'Philipp_Becker', 'Stijn_Koehler ', 'Jonas_Gauger', 'Adem_Tosun', 'Tut_Baldock', 'Daanish_Bambery', 'Alexander_Polidar', 'Beatriz_Oliveira', 'Maximilian_Erhardt', 'Tibor_Völcker', 'Halil_Demiralan', 'Jacopo_Ventura', 'Babu_Maddukuri', 'Thomas_Wüthrich', 
'Karl_Fuchs', 'Jeije_Van_den_Wijngaart', 'Virgile_Gautier', 'Thomas_Britting', 'Sebastian_Landsmann', 'Philip_Tzonev', 'Julian_Rimer', 'Ibrahim_Ata', 'Karina_Sapelnikova', 'Jonas_Kellner ', 'Daniil_Kedrinski', 'Daniel_Kussner', 'Thomas_Barouh', 'Florian_Eisele', 'Nick_Stein', 'Paul_Haufe', 'Michael_Hörmann', 'Eric_Brunner', 'Andreas_Engel', 'Nitin_Kumar', 'Lukas_Walter ', 'Melanie_Wullaert', 'Pierpaolo_Toniato ', 'David_Abplanalp', 'Marco_Desiderio', 'Yannick_Eydner', 'Trivendra_Kulhare', 'Léo_Bulckaen', 'Naveen_Gunasekaran', 'Stefano_Luca', 'Sydney_Dupasquier', 'Olgierd_Cichorek', 'Andreas_Tumbrink', 'Navin_Subramanian ', 'Monica_Arizaga', 'Guillaume_Lortie', 'Nicola_Zappacosta', 'Filipe_Barreiro', 'Calvin_Hooton', 'Joris_Kievits', 'Malte_Hauck', 'Tiago_Spieß', 'Alan_Saucedo', 'Jakhongir_Mamadov', 'Ponnaiyan_Ramasamy', 'Johannes_Benning', 'Sebastian_Schaeffler', 'Lars_van_der_Heijden', 'Julian_Busch', 'Peter_Nothofer', 'Marios_Karanikolidis', 'Dan_Thilderkvist', 'Sandro_Schönhoff', 'Zeljko_Pavlovic', 'Stefano_Centorame', 'Stefan_Panajotovic', 'Daniel_Severinsen', 'Pjotr_Lengkeek', 'Sammy_Ma', 'Praveen_Vasan', 'Phillip_Abplanalp ', 'Atef_Ghalayini ', 'Amr_Ibrahim', 'Jonathan_Panchyrz', 'Rudra']
           thisname = request.POST.get('empname')
           thisweek = int(request.POST.get('currentweek'))
           password = request.POST.get('password')
           admin_pass = "RFA10Spacex0"
           objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])

           objects2 = timeTracking.objects.values()
           df = pd.DataFrame( columns = [ 'empname', 'department', 'currentweek', 'day1', 'time_worked1', 'systemcode1', 'development_phase1', 'project1', 'day2', 'time_worked2', 'systemcode2', 'development_phase2', 'project2', 'day3', 'time_worked3', 'systemcode3', 'development_phase3', 'project3', 'day4', 'time_worked4', 'systemcode4', 'development_phase4', 'project4', 'day5', 'time_worked5', 'systemcode5', 'development_phase5', 'project5', 'day6', 'time_worked6', 'systemcode6', 'development_phase6', 'project6'  ])
           df['day1'] = pd.to_datetime(df['day1'], format= '%Y%m%d')
           df['day2'] = pd.to_datetime(df['day2'], format= '%Y%m%d')
           df['day3'] = pd.to_datetime(df['day3'], format= '%Y%m%d')
           df['day4'] = pd.to_datetime(df['day4'], format= '%Y%m%d')
           df['day5'] = pd.to_datetime(df['day5'], format= '%Y%m%d')
           df['day6'] = pd.to_datetime(df['day6'], format= '%Y%m%d')
           
           df = pd.DataFrame(list(objects2))
           #df = df.loc[(df['empname'] == thisname)]

           df['day1'] = df['day1'].astype(str)
           df['day2'] = df['day2'].astype(str)
           df['day3'] = df['day3'].astype(str)
           df['day4'] = df['day4'].astype(str)
           df['day5'] = df['day5'].astype(str)
           df['day6'] = df['day6'].astype(str)

           df_master = pd.DataFrame ( columns = ['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked'])
           
           df_1 = pd.DataFrame(columns =['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked'] )
           df_2 = pd.DataFrame(columns =['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked'] )
           df_3 = pd.DataFrame(columns =['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked'] )
           df_4 = pd.DataFrame(columns =['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked'] )
           df_5 = pd.DataFrame(columns =['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked'] )
           df_6 = pd.DataFrame(columns =['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked'] )

           for emp in name_lists:
            
            if (emp in df['empname'].values ):
               df = df.loc[df['empname'] == emp]

               df_1[['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked']] = df[[ 'empname', 'department', 'currentweek', 'project1', 'development_phase1', 'systemcode1', 'day1', 'time_worked1']]
               df_2[['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked']] = df[['empname', 'department', 'currentweek','project2', 'development_phase2', 'systemcode2', 'day2', 'time_worked2']]
               df_3[['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked']] = df[['empname', 'department', 'currentweek','project3', 'development_phase3', 'systemcode3', 'day3', 'time_worked3']]
               df_4[['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked']] = df[['empname', 'department', 'currentweek','project4', 'development_phase4', 'systemcode4', 'day4', 'time_worked4']]
               df_5[['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked']] = df[['empname', 'department', 'currentweek','project5', 'development_phase5', 'systemcode5', 'day5', 'time_worked5']]
               df_6[['empname', 'department', 'currentweek', 'project','development_phase', 'systemcode', 'date', 'time_worked']] = df[['empname', 'department', 'currentweek','project6', 'development_phase6', 'systemcode6', 'day6', 'time_worked6']]

           
               df_1 = df_1.append([df_2, df_3, df_4, df_5, df_6])
               df_1 = df_1.sort_values('currentweek')
               df_master = df_master.append(df_1)
               df_master['date'] = df_master['date'].astype(str)
               
               df_master = df_master[ df_master['date'] != 'None']
               df_master.reset_index(drop = True, inplace = True)
               

               df_1 = df_1[0:0]
               df_2 = df_2[0:0]
               df_3 = df_3[0:0]
               df_4 = df_4[0:0]
               df_5 = df_5[0:0]
               df_6 = df_6[0:0]

               df = pd.DataFrame(list(objects2))
               print(emp)
            else:
               continue

           print(df_master)
               
            
           
         
           
           if( password != '' and password == admin_pass): 
               response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
               response['Content-Disposition'] = 'attachment; filename="Master_data.xlsx"'                                        
               df_master.to_excel(response)
               return response
           else:
              
              empname = request.POST.get('empname')
            
              new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
              messages.success(request, "You need a valid Password to access the master Database!!")
              return render(request, 'display.html', {"name": empname, "data": new_objects})


        
        elif request.POST.get('empname') and request.POST.get('currentweek') and request.POST.get('submit'):
            thisname = request.POST.get('empname')
            thisweek = int(request.POST.get('currentweek'))
            objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            sys1 = timeTracking.objects.raw( 'SELECT id, systemcode1 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            sys2 = timeTracking.objects.raw( 'SELECT id, systemcode2 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            sys3 = timeTracking.objects.raw( 'SELECT id, systemcode3 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            sys4 = timeTracking.objects.raw( 'SELECT id,  systemcode4 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            sys5 = timeTracking.objects.raw( 'SELECT id, systemcode5 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            sys6 = timeTracking.objects.raw( 'SELECT id, systemcode6 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            tw1 = timeTracking.objects.raw( 'SELECT id, time_worked1 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            tw2 = timeTracking.objects.raw( 'SELECT id, time_worked2 AS sum1 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            tw3 = timeTracking.objects.raw( 'SELECT id, time_worked3 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            tw4 = timeTracking.objects.raw( 'SELECT id, time_worked4 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            tw5 = timeTracking.objects.raw( 'SELECT id, time_worked5 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])
            tw6 = timeTracking.objects.raw( 'SELECT id, time_worked6 FROM time_history WHERE empname = %s and currentweek = %s ', [thisname, thisweek])

            Total_tw1 = 0
            Total_tw2 = 0
            Total_tw3 = 0
            Total_tw4 = 0
            Total_tw5 = 0
            Total_tw6 = 0

            for t in tw1:
                if (t.time_worked1 != None):
                    Total_tw1 = t.time_worked1 + Total_tw1
            for t in tw2:
                if (t.time_worked2 != None):
                    Total_tw2 = t.time_worked2 + Total_tw2
            for t in tw3:
                if (t.time_worked3 != None):
                    Total_tw3 = t.time_worked3 + Total_tw3
            for t in tw4:
                if (t.time_worked4 != None):
                    Total_tw4 = t.time_worked4 + Total_tw4
            for t in tw5:
                if (t.time_worked5 != None):
                    Total_tw5 = t.time_worked5 + Total_tw5
            for t in tw6:
                if (t.time_worked6 != None):
                    Total_tw6 = t.time_worked6 + Total_tw6
                    

            now = datetime.datetime.now()
            today = (now.strftime("%A"))

             
            systemcodes = []
           
            for sys in sys1:
                systemcodes.append(sys.systemcode1)
              
            for sys in sys2:
                systemcodes.append(sys.systemcode2)
               
            for sys in sys3:
                systemcodes.append(sys.systemcode3)
               
            for sys in sys4:
                systemcodes.append(sys.systemcode4)
                
            for sys in sys5:
                systemcodes.append(sys.systemcode5)
               
            for sys in sys6:
                systemcodes.append(sys.systemcode6)
               
            unique_syscode = list(set(systemcodes))
            
            syscode_length= []
            for x in range(len(systemcodes)):
                syscode_length.append(x)
              
            sys_days = []
            for sys_codes in unique_syscode: 
                sys_days.append(timeTracking.objects.raw( 'SELECT id,time_worked1, time_worked2, time_worked3, time_worked4,time_worked5,time_worked6 FROM time_history WHERE empname = %s and currentweek = %s and systemcode1 = %s or systemcode2 = %s or  systemcode3 = %s  or systemcode4 = %s or systemcode5 = %s or systemcode6 = %s', [thisname, thisweek, sys_codes] ))
            

            day1 = day2 = day3 = day4 = day5 = day6 = day7 = None
            for object in objects:
                if object.day6 != None :
                  if object.day1 != None:
                    day1 = object.day1 
                  if object.day2 != None:
                    day2 = object.day2
                  if object.day3 != None:
                    day3 = object.day3
                  if object.day4 != None:
                    day4 = object.day4
                if object.day5 != None:
                    day5 = object.day5
                if object.day6 != None:
                    day6 = object.day6

                elif object.day5 != None :
                  if object.day1 != None:
                    day1 = object.day1
                  if object.day2 != None:
                    day2 = object.day2
                  if object.day3 != None:
                    day3 = object.day3
                  if object.day4 != None:
                    day4 = object.day4
                  if object.day5 != None:
                    day5 = object.day5

                elif object.day4 != None :
                  if object.day1 != None:
                    day1 = object.day1
                  if object.day2 != None:
                    day2 = object.day2
                  if object.day3 != None:
                    day3 = object.day3
                  if object.day4 != None:
                    day4 = object.day4
                
                elif object.day3 != None :
                  if object.day1 != None:
                    day1 = object.day1
                  if object.day2 != None:
                    day2 = object.day2
                  if object.day3 != None:
                    day3 = object.day3

                elif object.day2 != None :
                  if object.day1 != None:
                    day1 = object.day1
                  if object.day2 != None:
                    day2 = object.day2

                elif object.day1 != None :
                    day1 = object.day1
              
                else:
                    day1 = day2 = day3 = day4 = day5 = day6 = day7 = None
                
            


            return render(request, 'display.html', {"name": thisname,  "data": objects, "day1" : day1, "day2" : day2, "day3" : day3, "day4" : day4, "day5" : day5, "day6" : day6, "day7" : day7, "sys1": sys1, "sys2":sys2, "sys3":sys3, "sys4":sys4, "sys5":sys5, "sys6":sys6, "unique_syscode": unique_syscode, "syscode_length": syscode_length, "Total_tw1": Total_tw1, "Total_tw2": Total_tw2,"Total_tw3": Total_tw3,"Total_tw4": Total_tw4,"Total_tw5": Total_tw5,"Total_tw6": Total_tw6, "currentweek": thisweek  })
        

        else:
            
            empname = request.POST.get('empname')
            
            new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])
            messages.success(request, "Name not found in the Database!!")
            return render(request, 'display.html', {"name": empname, "data": new_objects})



    else:
        return render(request, 'display.html')


def delete(request, currentweek):
    deleted = timeTracking.objects.filter( currentweek = currentweek)
    deleted.delete()
    empname = request.GET.get('empname')
    new_objects = timeTracking.objects.raw( 'SELECT * FROM time_history WHERE empname = %s', [empname])

    return render(request, 'display.html', {"name": empname, "data": new_objects})






def delete_sys(request, id, empname, currentweek):
            deleted = timeTracking.objects.filter( id = id)
            deleted.delete()
    
            name = empname
            currentweek = currentweek



            return redirect( reverse('display' ))
            
def read_file(request):

    if (request.method == 'GET'):

       if(request.GET.get('email') and request.GET.get('send')):
           email = request.GET.get('email')
           return render(request, 'bootstrap_test.html', {"data" : email})
       else:
           email = "none"
           return render(request, 'bootstrap_test.html', {"data" : email})
    else:
        return render(request, 'bootstrap_test.html', {"data" : "something went wrong"})



