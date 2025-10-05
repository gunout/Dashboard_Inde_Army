# dashboard_defense_inde_avance.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page
st.set_page_config(
    page_title="Analyse Stratégique Avancée - Inde",
    page_icon="🐘",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avancé
st.markdown("""
<style>
    .main-header {
        font-size: 2.8rem;
        background: linear-gradient(45deg, #FF9933, #FFFFFF, #138808);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .metric-card {
        background: linear-gradient(135deg, #FF9933, #FF671F);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .section-header {
        color: #FF671F;
        border-bottom: 3px solid #138808;
        padding-bottom: 0.8rem;
        margin-top: 2rem;
        font-size: 1.8rem;
        font-weight: bold;
    }
    .nuclear-card {
        background: linear-gradient(135deg, #138808, #1A5E1A);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .navy-card {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .air-force-card {
        background: linear-gradient(135deg, #0066CC, #0080FF);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .army-card {
        background: linear-gradient(135deg, #8B4513, #A0522D);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .strategic-card {
        background: linear-gradient(135deg, #4B0082, #8A2BE2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .cyber-card {
        background: linear-gradient(135deg, #2d3436, #636e72);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class DefenseIndeDashboardAvance:
    def __init__(self):
        self.branches_options = self.define_branches_options()
        self.programmes_options = self.define_programmes_options()
        self.missile_systems = self.define_missile_systems()
        self.naval_assets = self.define_naval_assets()
        
    def define_branches_options(self):
        return [
            "Forces Armées Indiennes", "Armée de Terre Indienne", "Marine Indienne", 
            "Force Aérienne Indienne", "Forces Stratégiques", "Garde Côtière Indienne",
            "Forces Spéciales", "Commandement des Forces Intégrées"
        ]
    
    def define_programmes_options(self):
        return [
            "Programme Nucléaire Stratégique", "Modernisation des Forces", 
            "Make in India - Défense", "Défense Aérienne Intégrée",
            "Maritime Domain Awareness", "Cybersécurité", "Espace Militaire"
        ]
    
    def define_missile_systems(self):
        return {
            "Agni-V": {"type": "ICBM", "portee": 5000, "ogives": 3, "statut": "Opérationnel"},
            "Agni-IV": {"type": "IRBM", "portee": 4000, "ogives": 1, "statut": "Opérationnel"},
            "Agni-III": {"type": "IRBM", "portee": 3000, "ogives": 1, "statut": "Opérationnel"},
            "Prithvi-II": {"type": "MRBM", "portee": 350, "ogives": "Conventionnelle/Nucléaire", "statut": "Opérationnel"},
            "BrahMos": {"type": "Missile de Croisière", "portee": 450, "vitesse": "Mach 2.8", "statut": "Opérationnel"}
        }
    
    def define_naval_assets(self):
        return {
            "INS Vikramaditya": {"type": "Porte-avions", "deplacement": 45000, "avions": 36, "statut": "Opérationnel"},
            "INS Vikrant": {"type": "Porte-avions", "deplacement": 40000, "avions": 30, "statut": "Opérationnel"},
            "INS Kolkata": {"type": "Destroyer", "deplacement": 7500, "armement": "Brahmos", "statut": "Opérationnel"},
            "INS Arihant": {"type": "Sous-marin Nucléaire", "deplacement": 6000, "missiles": "K-15", "statut": "Opérationnel"},
            "INS Chakra": {"type": "Sous-marin Nucléaire", "deplacement": 8000, "torpilles": "Type 53", "statut": "Opérationnel"}
        }
    
    def generate_advanced_data(self, selection):
        """Génère des données avancées et détaillées pour l'Inde"""
        annees = list(range(2000, 2028))
        
        config = self.get_advanced_config(selection)
        
        data = {
            'Annee': annees,
            'Budget_Defense_Mds': self.simulate_advanced_budget(annees, config),
            'Personnel_Milliers': self.simulate_advanced_personnel(annees, config),
            'PIB_Militaire_Pourcent': self.simulate_military_gdp_percentage(annees),
            'Exercices_Militaires': self.simulate_advanced_exercises(annees, config),
            'Readiness_Operative': self.simulate_advanced_readiness(annees),
            'Capacite_Dissuasion': self.simulate_advanced_deterrence(annees),
            'Temps_Mobilisation_Jours': self.simulate_advanced_mobilization(annees),
            'Tests_Missiles': self.simulate_missile_tests(annees),
            'Developpement_Technologique': self.simulate_tech_development(annees),
            'Capacite_Artillerie': self.simulate_artillery_capacity(annees),
            'Couverture_AD': self.simulate_air_defense_coverage(annees),
            'Resilience_Logistique': self.simulate_logistical_resilience(annees),
            'Cyber_Capabilities': self.simulate_cyber_capabilities(annees),
            'Production_Armements': self.simulate_weapon_production(annees)
        }
        
        # Données spécifiques aux programmes
        if 'nucleaire' in config.get('priorites', []):
            data.update({
                'Stock_Ogives_Nucleaires': self.simulate_nuclear_arsenal_size(annees),
                'Portee_Max_Missiles_Km': self.simulate_missile_range_evolution(annees),
                'Capacite_Sous_Marine': self.simulate_submarine_capability(annees),
                'Essais_Souterrains': self.simulate_underground_tests(annees)
            })
        
        if 'modernisation' in config.get('priorites', []):
            data.update({
                'Nouveaux_Systemes': self.simulate_new_systems(annees),
                'Taux_Modernisation': self.simulate_modernization_rate(annees),
                'Exportations_Armes': self.simulate_weapon_exports(annees)
            })
        
        if 'maritime' in config.get('priorites', []):
            data.update({
                'Navires_Combat': self.simulate_naval_fleet(annees),
                'Portee_Projection_Nm': self.simulate_naval_range(annees),
                'Exercices_Combines': self.simulate_joint_exercises(annees)
            })
        
        if 'cyber' in config.get('priorites', []):
            data.update({
                'Attaques_Cyber_Reussies': self.simulate_cyber_attacks(annees),
                'Reseau_Commandement_Cyber': self.simulate_cyber_command(annees),
                'Cyber_Defense_Niveau': self.simulate_cyber_defense(annees)
            })
        
        return pd.DataFrame(data), config
    
    def get_advanced_config(self, selection):
        """Configuration avancée avec plus de détails pour l'Inde"""
        configs = {
            "Forces Armées Indiennes": {
                "type": "armee_totale",
                "budget_base": 70.0,
                "personnel_base": 1400,
                "exercices_base": 120,
                "priorites": ["nucleaire", "modernisation", "maritime", "cyber", "conventionnel"],
                "doctrines": ["Dissuasion Crédible", "Défense Active", "Riposte Massive"],
                "capacites_speciales": ["Forces Rapides", "Guerre Montagne", "Projection Maritime"]
            },
            "Forces Stratégiques": {
                "type": "branche_strategique",
                "personnel_base": 8,
                "exercices_base": 15,
                "priorites": ["triade_nucleaire", "missiles_balistiques", "sous_marins"],
                "systemes_deployes": ["Agni-V", "Agni-IV", "Arihant", "Rafale"],
                "commandement": "Commandement des Forces Stratégiques"
            },
            "Marine Indienne": {
                "type": "branche_navale",
                "personnel_base": 67,
                "exercices_base": 40,
                "priorites": ["porte_avions", "sous_marins", "lutte_anti_sous_marine", "projection"],
                "flottes_principales": ["Flotte Orientale", "Flotte Occidentale", "Flotte du Sud"],
                "navires_cles": ["Vikramaditya", "Vikrant", "Kolkata", "Arihant"]
            },
            "Programme Nucléaire Stratégique": {
                "type": "programme_strategique",
                "budget_base": 2.5,
                "priorites": ["triade_nucleaire", "missiles_intercontinentaux", "sous_marins"],
                "composantes": ["Forces Terrestres", "Forces Aériennes", "Forces Navales"],
                "doctrine": "No First Use - Riposte Massive"
            }
        }
        
        return configs.get(selection, {
            "type": "branche",
            "personnel_base": 100,
            "exercices_base": 25,
            "priorites": ["defense_generique"]
        })
    
    def simulate_advanced_budget(self, annees, config):
        """Simulation avancée du budget avec variations géopolitiques"""
        budget_base = config.get('budget_base', 60.0)
        budgets = []
        for annee in annees:
            base = budget_base * (1 + 0.065 * (annee - 2000))
            # Variations selon événements géopolitiques
            if 2002 <= annee <= 2004:  # Tensions avec le Pakistan
                base *= 1.1
            elif 2008 <= annee <= 2010:  # Modernisation accélérée
                base *= 1.15
            elif annee >= 2016:  # Make in India
                base *= 1.2
            elif annee >= 2020:  # Tensions avec la Chine
                base *= 1.25
            budgets.append(base)
        return budgets
    
    def simulate_advanced_personnel(self, annees, config):
        """Simulation avancée des effectifs"""
        personnel_base = config.get('personnel_base', 1300)
        return [personnel_base * (1 + 0.008 * (annee - 2000)) for annee in annees]
    
    def simulate_military_gdp_percentage(self, annees):
        """Pourcentage du PIB consacré à la défense"""
        return [2.5 + 0.1 * (annee - 2000) for annee in annees]
    
    def simulate_advanced_exercises(self, annees, config):
        """Exercices militaires avec saisonnalité"""
        base = config.get('exercices_base', 80)
        return [base + 4 * (annee - 2000) + 8 * np.sin(2 * np.pi * (annee - 2000)/4) for annee in annees]
    
    def simulate_advanced_readiness(self, annees):
        """Préparation opérationnelle avancée"""
        readiness = []
        for annee in annees:
            base = 65 + 1.5 * (annee - 2000)
            if annee >= 2008:  # Réformes post-26/11
                base += 8
            if annee >= 2014:  # Modernisation
                base += 7
            if annee >= 2020:  # Expérience opérationnelle
                base += 5
            readiness.append(min(base, 90))
        return readiness
    
    def simulate_advanced_deterrence(self, annees):
        """Capacité de dissuasion avancée"""
        deterrence = []
        for annee in annees:
            if annee < 1998:
                base = 0  # Pré-nucléaire
            elif annee < 2003:
                base = 40  # Capacité nucléaire basique
            elif annee < 2012:
                base = 60  # Missiles balistiques
            elif annee < 2018:
                base = 75  # Triade en développement
            else:
                base = 85 + 1 * (annee - 2018)  # Triade opérationnelle
            deterrence.append(min(base, 95))
        return deterrence
    
    def simulate_advanced_mobilization(self, annees):
        """Temps de mobilisation avancé"""
        return [max(45 - 1 * (annee - 2000), 15) for annee in annees]
    
    def simulate_missile_tests(self, annees):
        """Tests de missiles"""
        tests = []
        for annee in annees:
            if annee < 2006:
                tests.append(2)
            elif annee < 2012:
                tests.append(4 + (annee - 2006))
            else:
                tests.append(10 + 2 * (annee - 2012))
        return tests
    
    def simulate_tech_development(self, annees):
        """Développement technologique global"""
        return [min(50 + 2.5 * (annee - 2000), 85) for annee in annees]
    
    def simulate_artillery_capacity(self, annees):
        """Capacité d'artillerie"""
        return [min(70 + 1.8 * (annee - 2000), 90) for annee in annees]
    
    def simulate_air_defense_coverage(self, annees):
        """Couverture de défense anti-aérienne"""
        return [min(55 + 2.2 * (annee - 2000), 88) for annee in annees]
    
    def simulate_logistical_resilience(self, annees):
        """Résilience logistique"""
        return [min(60 + 2 * (annee - 2000), 87) for annee in annees]
    
    def simulate_cyber_capabilities(self, annees):
        """Capacités cybernétiques"""
        return [min(45 + 3 * (annee - 2000), 82) for annee in annees]
    
    def simulate_weapon_production(self, annees):
        """Production d'armements (indice)"""
        return [min(55 + 2.8 * (annee - 2000), 89) for annee in annees]
    
    def simulate_nuclear_arsenal_size(self, annees):
        """Évolution du stock d'ogives nucléaires"""
        stock = []
        for annee in annees:
            if annee < 1998:
                stock.append(0)
            elif annee < 2005:
                stock.append(50 + 5 * (annee - 1998))
            elif annee < 2015:
                stock.append(80 + 8 * (annee - 2005))
            else:
                stock.append(150 + 10 * (annee - 2015))
        return [min(s, 300) for s in stock]
    
    def simulate_missile_range_evolution(self, annees):
        """Évolution de la portée maximale des missiles"""
        portee = []
        for annee in annees:
            if annee < 2002:
                portee.append(250)  # Prithvi
            elif annee < 2007:
                portee.append(700 + 200 * (annee - 2002))  # Agni-I/II
            elif annee < 2012:
                portee.append(2000 + 500 * (annee - 2007))  # Agni-III
            elif annee < 2018:
                portee.append(3500 + 500 * (annee - 2012))  # Agni-IV
            else:
                portee.append(5000)  # Agni-V
        return portee
    
    def simulate_submarine_capability(self, annees):
        """Capacité sous-marine stratégique"""
        return [min(20 + 4 * (annee - 2009), 85) for annee in annees if annee >= 2009] + [0] * (2009 - min(annees))
    
    def simulate_underground_tests(self, annees):
        """Essais souterrains et préparation"""
        return [min(60 + 2 * (annee - 2000), 90) for annee in annees]
    
    def simulate_new_systems(self, annees):
        """Nouveaux systèmes déployés"""
        return [min(3 + 1.5 * (annee - 2000), 40) for annee in annees]
    
    def simulate_modernization_rate(self, annees):
        """Taux de modernisation des équipements"""
        return [min(25 + 3.5 * (annee - 2000), 80) for annee in annees]
    
    def simulate_weapon_exports(self, annees):
        """Exportations d'armes (milliards USD)"""
        return [min(0.1 + 0.3 * (annee - 2000), 3) for annee in annees]
    
    def simulate_naval_fleet(self, annees):
        """Flotte navale de combat"""
        return [min(25 + 2 * (annee - 2000), 70) for annee in annees]
    
    def simulate_naval_range(self, annees):
        """Portée de projection navale"""
        return [min(500 + 50 * (annee - 2000), 2000) for annee in annees]
    
    def simulate_joint_exercises(self, annees):
        """Exercices combinés avec partenaires"""
        return [min(5 + 2 * (annee - 2000), 35) for annee in annees]
    
    def simulate_cyber_attacks(self, annees):
        """Attaques cyber réussies (estimation)"""
        return [min(10 + 2 * (annee - 2000), 60) for annee in annees]
    
    def simulate_cyber_command(self, annees):
        """Réseau de commandement cyber"""
        return [min(40 + 3 * (annee - 2000), 85) for annee in annees]
    
    def simulate_cyber_defense(self, annees):
        """Capacités de cyber défense"""
        return [min(45 + 2.8 * (annee - 2000), 83) for annee in annees]
    
    def display_advanced_header(self):
        """En-tête avancé avec plus d'informations"""
        st.markdown('<h1 class="main-header">🐘 ANALYSE STRATÉGIQUE AVANCÉE - RÉPUBLIQUE DE L\'INDE</h1>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; background: linear-gradient(135deg, #FF9933, #138808); 
            padding: 1rem; border-radius: 10px; color: white; margin: 1rem 0;'>
            <h3>🛡️ SYSTÈME DE DÉFENSE INTÉGRÉ DE LA RÉPUBLIQUE DE L'INDE</h3>
            <p><strong>Analyse multidimensionnelle des capacités militaires et stratégiques (2000-2027)</strong></p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_advanced_sidebar(self):
        """Sidebar avancé avec plus d'options"""
        st.sidebar.markdown("## 🎛️ PANEL DE CONTRÔLE AVANCÉ")
        
        # Sélection du type d'analyse
        type_analyse = st.sidebar.radio(
            "Mode d'analyse:",
            ["Analyse Branche Militaire", "Programmes Stratégiques", "Vue Systémique", "Scénarios Géopolitiques"]
        )
        
        if type_analyse == "Analyse Branche Militaire":
            selection = st.sidebar.selectbox("Branche militaire:", self.branches_options)
        elif type_analyse == "Programmes Stratégiques":
            selection = st.sidebar.selectbox("Programme stratégique:", self.programmes_options)
        elif type_analyse == "Vue Systémique":
            selection = "Forces Armées Indiennes"
        else:
            selection = "Scénarios Géopolitiques"
        
        # Options avancées
        st.sidebar.markdown("### 🔧 OPTIONS AVANCÉES")
        show_geopolitical = st.sidebar.checkbox("Contexte géopolitique", value=True)
        show_doctrinal = st.sidebar.checkbox("Analyse doctrinale", value=True)
        show_technical = st.sidebar.checkbox("Détails techniques", value=True)
        threat_assessment = st.sidebar.checkbox("Évaluation des menaces", value=True)
        
        # Paramètres de simulation
        st.sidebar.markdown("### ⚙️ PARAMÈTRES DE SIMULATION")
        scenario = st.sidebar.selectbox("Scénario:", ["Statut Quo", "Tensions Chine", "Modernisation Accélérée", "Conflit Régional"])
        
        return {
            'selection': selection,
            'type_analyse': type_analyse,
            'show_geopolitical': show_geopolitical,
            'show_doctrinal': show_doctrinal,
            'show_technical': show_technical,
            'threat_assessment': threat_assessment,
            'scenario': scenario
        }
    
    def display_strategic_metrics(self, df, config):
        """Métriques stratégiques avancées"""
        st.markdown('<h3 class="section-header">🎯 TABLEAU DE BORD STRATÉGIQUE</h3>', 
                   unsafe_allow_html=True)
        
        derniere_annee = df['Annee'].max()
        data_actuelle = df[df['Annee'] == derniere_annee].iloc[0]
        data_2000 = df[df['Annee'] == 2000].iloc[0]
        
        # Première ligne de métriques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>💰 BUDGET DÉFENSE 2027</h4>
                <h2>{:.1f} Md$</h2>
                <p>📈 {:.1f}% du PIB</p>
            </div>
            """.format(data_actuelle['Budget_Defense_Mds'], data_actuelle['PIB_Militaire_Pourcent']), 
            unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>👥 EFFECTIFS TOTAUX</h4>
                <h2>{:,.0f}K</h2>
                <p>⚔️ +{:.1f}% depuis 2000</p>
            </div>
            """.format(data_actuelle['Personnel_Milliers'], 
                     ((data_actuelle['Personnel_Milliers'] - data_2000['Personnel_Milliers']) / data_2000['Personnel_Milliers']) * 100), 
            unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="nuclear-card">
                <h4>☢️ TRIADE NUCLÉAIRE</h4>
                <h2>{:.0f}%</h2>
                <p>🚀 {} ogives stratégiques</p>
            </div>
            """.format(data_actuelle['Capacite_Dissuasion'], 
                     int(data_actuelle.get('Stock_Ogives_Nucleaires', 0))), 
            unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="strategic-card">
                <h4>🌊 PUISSANCE NAVALE</h4>
                <h2>{:.0f}%</h2>
                <p>⚓ {} navires majeurs</p>
            </div>
            """.format(data_actuelle.get('Portee_Projection_Nm', 0)/20, 
                     int(data_actuelle.get('Navires_Combat', 0))), 
            unsafe_allow_html=True)
        
        # Deuxième ligne de métriques
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            reduction_temps = ((data_2000['Temps_Mobilisation_Jours'] - data_actuelle['Temps_Mobilisation_Jours']) / 
                             data_2000['Temps_Mobilisation_Jours']) * 100
            st.metric(
                "⏱️ Temps Mobilisation",
                f"{data_actuelle['Temps_Mobilisation_Jours']:.1f} jours",
                f"{reduction_temps:+.1f}%"
            )
        
        with col6:
            croissance_ad = ((data_actuelle['Couverture_AD'] - data_2000['Couverture_AD']) / 
                           data_2000['Couverture_AD']) * 100
            st.metric(
                "🛡️ Défense Anti-Aérienne",
                f"{data_actuelle['Couverture_AD']:.1f}%",
                f"{croissance_ad:+.1f}%"
            )
        
        with col7:
            if 'Portee_Max_Missiles_Km' in df.columns:
                croissance_portee = ((data_actuelle['Portee_Max_Missiles_Km'] - data_2000.get('Portee_Max_Missiles_Km', 250)) / 
                                   data_2000.get('Portee_Max_Missiles_Km', 250)) * 100
                st.metric(
                    "🎯 Portée Missiles Max",
                    f"{data_actuelle['Portee_Max_Missiles_Km']:,.0f} km",
                    f"{croissance_portee:+.1f}%"
                )
        
        with col8:
            st.metric(
                "📊 Préparation Opérationnelle",
                f"{data_actuelle['Readiness_Operative']:.1f}%",
                f"+{(data_actuelle['Readiness_Operative'] - data_2000['Readiness_Operative']):.1f}%"
            )
    
    def create_comprehensive_analysis(self, df, config):
        """Analyse complète multidimensionnelle"""
        st.markdown('<h3 class="section-header">📊 ANALYSE MULTIDIMENSIONNELLE</h3>', 
                   unsafe_allow_html=True)
        
        # Graphiques principaux
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution des capacités principales
            fig = go.Figure()
            
            capacites = ['Readiness_Operative', 'Capacite_Dissuasion', 'Cyber_Capabilities', 'Couverture_AD']
            noms = ['Préparation Opér.', 'Dissuasion Strat.', 'Capacités Cyber', 'Défense Anti-Aérienne']
            couleurs = ['#FF9933', '#138808', '#2d3436', '#4B0082']
            
            for i, (cap, nom, couleur) in enumerate(zip(capacites, noms, couleurs)):
                if cap in df.columns:
                    fig.add_trace(go.Scatter(
                        x=df['Annee'], y=df[cap],
                        mode='lines', name=nom,
                        line=dict(color=couleur, width=4),
                        hovertemplate=f"{nom}: %{{y:.1f}}%<extra></extra>"
                    ))
            
            fig.update_layout(
                title="📈 ÉVOLUTION DES CAPACITÉS STRATÉGIQUES (2000-2027)",
                xaxis_title="Année",
                yaxis_title="Niveau de Capacité (%)",
                height=500,
                template="plotly_white",
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse des programmes stratégiques
            strategic_data = []
            strategic_names = []
            
            if 'Stock_Ogives_Nucleaires' in df.columns:
                strategic_data.append(df['Stock_Ogives_Nucleaires'])
                strategic_names.append('Stock Ogives Nucléaires')
            
            if 'Tests_Missiles' in df.columns:
                strategic_data.append(df['Tests_Missiles'])
                strategic_names.append('Tests de Missiles')
            
            if 'Navires_Combat' in df.columns:
                strategic_data.append(df['Navires_Combat'])
                strategic_names.append('Navires de Combat')
            
            if strategic_data:
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                for i, (data, nom) in enumerate(zip(strategic_data, strategic_names)):
                    fig.add_trace(
                        go.Scatter(x=df['Annee'], y=data, name=nom,
                                 line=dict(width=4)),
                        secondary_y=(i > 0)
                    )
                
                fig.update_layout(
                    title="🚀 PROGRAMMES STRATÉGIQUES - ÉVOLUTION COMPARÉE",
                    height=500,
                    template="plotly_white"
                )
                st.plotly_chart(fig, use_container_width=True)
    
    def create_geopolitical_analysis(self, df, config):
        """Analyse géopolitique avancée"""
        st.markdown('<h3 class="section-header">🌍 CONTEXTE GÉOPOLITIQUE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Cartes des zones stratégiques
            st.markdown("""
            <div class="nuclear-card">
                <h4>🎯 ENJEUX STRATÉGIQUES RÉGIONAUX</h4>
                <p><strong>Frontière Chine:</strong> LAC - Line of Actual Control</p>
                <p><strong>Frontière Pakistan:</strong> LoC - Line of Control</p>
                <p><strong>Océan Indien:</strong> Zone d'influence maritime</p>
                <p><strong>Détroit de Malacca:</strong> Route commerciale vitale</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Analyse des relations internationales
            st.markdown("""
            <div class="strategic-card">
                <h4>🤝 RELATIONS INTERNATIONALES</h4>
                <p><strong>États-Unis:</strong> Partenariat stratégique (QUAD)</p>
                <p><strong>Russie:</strong> Partenaire militaire traditionnel</p>
                <p><strong>France:</strong> Coopération technologique avancée</p>
                <p><strong>Japon/Australie:</strong> Coopération indo-pacifique</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Analyse des tensions régionales
            tensions_data = {
                'Année': [1999, 2002, 2008, 2016, 2019, 2020, 2022],
                'Niveau_Tension': [8, 7, 6, 5, 6, 8, 7],  # sur 10
                'Conflit': ['Kargil', 'Parliament Attack', 'Mumbai', 'Uri', 'Pulwama', 'Galwan', 'LAC Skirmish']
            }
            tensions_df = pd.DataFrame(tensions_data)
            
            fig = px.line(tensions_df, x='Année', y='Niveau_Tension', 
                         title="📉 ÉVOLUTION DES TENSIONS RÉGIONALES",
                         labels={'Niveau_Tension': 'Niveau de Tension'},
                         markers=True)
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Indice de coopération internationale
            cooperation = [min(40 + 3 * (annee - 2000), 85) for annee in df['Annee']]
            fig = px.area(x=df['Annee'], y=cooperation,
                         title="🕊️ COOPÉRATION INTERNATIONALE - PARTENARIATS STRATÉGIQUES",
                         labels={'x': 'Année', 'y': 'Niveau de Coopération (%)'})
            fig.update_traces(fillcolor='rgba(19, 136, 8, 0.3)', line_color='#138808')
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
    
    def create_technical_analysis(self, df, config):
        """Analyse technique détaillée"""
        st.markdown('<h3 class="section-header">🔬 ANALYSE TECHNIQUE AVANCÉE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Analyse des systèmes d'armes
            systems_data = {
                'Système': ['Rafale', 'Sukhoi Su-30MKI', 'Agni-V', 'INS Vikrant', 
                           'BrahMos', 'Arjun MK-1A', 'Tejas MK-1A'],
                'Portée (km)': [3700, 3000, 5000, 7500, 450, 500, 3000],
                'Année Service': [2020, 2002, 2018, 2022, 2006, 2021, 2021],
                'Statut': ['Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel', 'Opérationnel']
            }
            systems_df = pd.DataFrame(systems_data)
            
            fig = px.scatter(systems_df, x='Portée (km)', y='Année Service', 
                           size='Portée (km)', color='Statut',
                           hover_name='Système', log_x=True,
                           title="🎯 CARACTÉRISTIQUES DES SYSTÈMES D'ARMES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Analyse de la modernisation
            modernization_data = {
                'Domaine': ['Forces Terrestres', 'Forces Stratégiques', 
                          'Défense Aérienne', 'Marine', 'Force Aérienne'],
                'Niveau 2000': [45, 30, 40, 35, 50],
                'Niveau 2027': [80, 85, 82, 78, 85]
            }
            modern_df = pd.DataFrame(modernization_data)
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='2000', x=modern_df['Domaine'], y=modern_df['Niveau 2000'],
                                marker_color='#FF9933'))
            fig.add_trace(go.Bar(name='2027', x=modern_df['Domaine'], y=modern_df['Niveau 2027'],
                                marker_color='#138808'))
            
            fig.update_layout(title="📈 MODERNISATION DES CAPACITÉS MILITAIRES",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
            
            # Cartographie des installations
            st.markdown("""
            <div class="strategic-card">
                <h4>🗺️ INSTALLATIONS STRATÉGIQUES CLÉS</h4>
                <p><strong>Western Naval Command:</strong> Mumbai</p>
                <p><strong>Eastern Naval Command:</strong> Visakhapatnam</p>
                <p><strong>Strategic Forces Command:</strong> New Delhi</p>
                <p><strong>Mountain Strike Corps:</strong> Panagarh</p>
            </div>
            """, unsafe_allow_html=True)
    
    def create_doctrinal_analysis(self, config):
        """Analyse doctrinale avancée"""
        st.markdown('<h3 class="section-header">📚 ANALYSE DOCTRINALE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="nuclear-card">
                <h4>🎯 DOCTRINE NUCLÉAIRE</h4>
                <p><strong>No First Use:</strong> Non-emploi en premier</p>
                <p><strong>Dissuasion crédible:</strong> Riposte massive</p>
                <p><strong>Triade nucléaire:</strong> Terre, air, mer</p>
                <p><strong>Contrôle civil:</strong> Autorité politique</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="strategic-card">
                <h4>⚡ DOCTRINE DE DÉFENSE ACTIVE</h4>
                <p><strong>Cold Start:</strong> Réponse rapide limitée</p>
                <p><strong>Défense en profondeur:</strong> Défense échelonnée</p>
                <p><strong>Mobilité stratégique:</strong> Rapidité de déploiement</p>
                <p><strong>Coordination interarmes:</strong> Synergie des forces</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="air-force-card">
                <h4>🌊 DOCTRINE MARITIME</h4>
                <p><strong>Sea Control:</strong> Contrôle des voies maritimes</p>
                <p><strong>Sea Denial:</strong> Déni d'accès à l'adversaire</p>
                <p><strong>Projection de puissance:</strong> Force expéditionnaire</p>
                <p><strong>Coopération régionale:</strong> Sécurité collective</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Principes opérationnels
        st.markdown("""
        <div class="navy-card">
            <h4>🎖️ PRINCIPES OPÉRATIONNELS DES FORCES ARMÉES INDIENNES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Unité de commandement:</strong> Coordination centralisée</div>
                <div><strong>• Mobilité et surprise:</strong> Opérations rapides</div>
                <div><strong>• Utilisation du terrain:</strong> Avantage montagneux</div>
                <div><strong>• Guerre intégrée:</strong> Coordination interarmes</div>
                <div><strong>• Soutien logistique:</strong> Chaîne d'approvisionnement</div>
                <div><strong>• Préparation permanente:</strong> État d'alerte</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_threat_assessment(self, df, config):
        """Évaluation avancée des menaces"""
        st.markdown('<h3 class="section-header">⚠️ ÉVALUATION STRATÉGIQUE DES MENACES</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Matrice des menaces
            threats_data = {
                'Type de Menace': ['Conflit Chine', 'Conflit Pakistan', 'Terrorisme Transfrontalier', 
                                 'Guerre Cyber', 'Instabilité Maritime', 'Guerre de Montagne'],
                'Probabilité': [0.6, 0.7, 0.8, 0.9, 0.5, 0.6],
                'Impact': [0.8, 0.7, 0.6, 0.5, 0.6, 0.7],
                'Niveau Préparation': [0.8, 0.9, 0.7, 0.6, 0.7, 0.8]
            }
            threats_df = pd.DataFrame(threats_data)
            
            fig = px.scatter(threats_df, x='Probabilité', y='Impact', 
                           size='Niveau Préparation', color='Type de Menace',
                           title="🎯 MATRICE RISQUES - PROBABILITÉ VS IMPACT",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Capacités de réponse
            response_data = {
                'Scénario': ['Conflit Frontière Chine', 'Conflit Pakistan', 'Attaque Terroriste', 
                           'Crise Maritime', 'Guerre Cyber'],
                'Dissuasion': [0.8, 0.7, 0.3, 0.6, 0.4],
                'Défense': [0.7, 0.8, 0.6, 0.7, 0.5],
                'Riposte': [0.9, 0.9, 0.8, 0.8, 0.7]
            }
            response_df = pd.DataFrame(response_data)
            
            fig = go.Figure(data=[
                go.Bar(name='Dissuasion', x=response_df['Scénario'], y=response_df['Dissuasion']),
                go.Bar(name='Défense', x=response_df['Scénario'], y=response_df['Défense']),
                go.Bar(name='Riposte', x=response_df['Scénario'], y=response_df['Riposte'])
            ])
            fig.update_layout(title="🛡️ CAPACITÉS DE RÉPONSE PAR SCÉNARIO",
                             barmode='group', height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("""
        <div class="nuclear-card">
            <h4>🎯 RECOMMANDATIONS STRATÉGIQUES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div><strong>• Renforcement nucléaire:</strong> Compléter la triade</div>
                <div><strong>• Modernisation conventionnelle:</strong> Equipements avancés</div>
                <div><strong>• Défense aérienne:</strong> Systèmes intégrés</div>
                <div><strong>• Puissance navale:</strong> Projection dans l'océan Indien</div>
                <div><strong>• Cyber défense:</strong> Protection des infrastructures</div>
                <div><strong>• Autosuffisance:</strong> Programme Make in India</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    def create_missile_database(self):
        """Base de données des systèmes de missiles"""
        st.markdown('<h3 class="section-header">🚀 BASE DE DONNÉES DES SYSTÈMES DE MISSILES</h3>', 
                   unsafe_allow_html=True)
        
        missile_data = []
        for nom, specs in self.missile_systems.items():
            missile_data.append({
                'Système': nom,
                'Type': specs['type'],
                'Portée (km)': specs['portee'],
                'Ogives': specs.get('ogives', 'N/A'),
                'Statut': specs['statut'],
                'Vitesse': specs.get('vitesse', 'N/A')
            })
        
        missile_df = pd.DataFrame(missile_data)
        
        # Affichage interactif
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = px.scatter(missile_df, x='Portée (km)', y='Ogives',
                           size='Portée (km)', color='Type',
                           hover_name='Système', log_x=True,
                           title="🚀 CARACTÉRISTIQUES DES SYSTÈMES DE MISSILES",
                           size_max=30)
            fig.update_layout(height=500)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="nuclear-card">
                <h4>📋 INVENTAIRE MISSILISTIQUE</h4>
            """, unsafe_allow_html=True)
            
            for missile in missile_data:
                st.markdown(f"""
                <div style="background: rgba(255,255,255,0.1); padding: 0.5rem; margin: 0.2rem 0; border-radius: 5px;">
                    <strong>{missile['Système']}</strong><br>
                    🎯 {missile['Type']} • 🚀 {missile['Portée (km)']:,} km<br>
                    💣 {missile['Ogives']} • {missile['Statut']}
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    def run_advanced_dashboard(self):
        """Exécute le dashboard avancé complet"""
        # Sidebar avancé
        controls = self.create_advanced_sidebar()
        
        # Header avancé
        self.display_advanced_header()
        
        # Génération des données avancées
        df, config = self.generate_advanced_data(controls['selection'])
        
        # Navigation par onglets avancés
        tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
            "📊 Tableau de Bord", 
            "🔬 Analyse Technique", 
            "🌍 Contexte Géopolitique", 
            "📚 Doctrine Militaire",
            "⚠️ Évaluation Menaces",
            "🚀 Systèmes de Missiles",
            "💎 Synthèse Stratégique"
        ])
        
        with tab1:
            self.display_strategic_metrics(df, config)
            self.create_comprehensive_analysis(df, config)
        
        with tab2:
            self.create_technical_analysis(df, config)
        
        with tab3:
            if controls['show_geopolitical']:
                self.create_geopolitical_analysis(df, config)
        
        with tab4:
            if controls['show_doctrinal']:
                self.create_doctrinal_analysis(config)
        
        with tab5:
            if controls['threat_assessment']:
                self.create_threat_assessment(df, config)
        
        with tab6:
            if controls['show_technical']:
                self.create_missile_database()
        
        with tab7:
            self.create_strategic_synthesis(df, config, controls)
    
    def create_strategic_synthesis(self, df, config, controls):
        """Synthèse stratégique finale"""
        st.markdown('<h3 class="section-header">💎 SYNTHÈSE STRATÉGIQUE - RÉPUBLIQUE DE L\'INDE</h3>', 
                   unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="nuclear-card">
                <h4>🏆 POINTS FORTS STRATÉGIQUES</h4>
                <div style="margin-top: 1rem;">
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>☢️ Statut de Puissance Nucléaire</strong>
                        <p>Triade nucléaire en développement avec doctrine de non-emploi en premier</p>
                    </div>
                    <div class="navy-card" style="margin: 0.5rem 0;">
                        <strong>🌊 Puissance Navale Croissante</strong>
                        <p>Deux porte-avions opérationnels et flotte en modernisation accélérée</p>
                    </div>
                    <div class="air-force-card" style="margin: 0.5rem 0;">
                        <strong>✈️ Force Aérienne Moderne</strong>
                        <p>Mix d'avions occidentaux et russes avec développement de capacités indigènes</p>
                    </div>
                    <div class="army-card" style="margin: 0.5rem 0;">
                        <strong>🏔️ Expertise en Guerre de Montagne</strong>
                        <p>Forces spécialisées dans le combat en haute altitude et conditions extrêmes</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="strategic-card">
                <h4>🎯 DÉFIS ET VULNÉRABILITÉS</h4>
                <div style="margin-top: 1rem;">
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>💸 Dépendance aux Importations</strong>
                        <p>70% des équipements militaires encore importés malgré Make in India</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>🔧 Retards Technologiques</strong>
                        <p>Certains programmes indigènes connaissent des retards importants</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>🌐 Défis Logistiques</strong>
                        <p>Approvisionnement des forces dans les régions frontalières reculées</p>
                    </div>
                    <div class="strategic-card" style="margin: 0.5rem 0;">
                        <strong>⚡ Menaces Asymétriques</strong>
                        <p>Terrorisme transfrontalier et guerre hybride avec le Pakistan</p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Perspectives futures
        st.markdown("""
        <div class="metric-card">
            <h4>🔮 PERSPECTIVES STRATÉGIQUES 2027-2035</h4>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🚀 DOMAINE NUCLÉAIRE</h5>
                    <p>• Triade nucléaire complète<br>• Missiles Agni-VI<br>• Sous-marins Arihant avancés<br>• Bombardiers stratégiques</p>
                </div>
                <div>
                    <h5>🌊 PUISSANCE NAVALE</h5>
                    <p>• 3ème porte-avions indigène<br>• 6 sous-marins nucléaires<br>• Destroyers de nouvelle génération<br>• Base aéronavale dans les Andaman</p>
                </div>
                <div>
                    <h5>💻 TECHNOLOGIES AVANCÉES</h5>
                    <p>• AMCA 5ème génération<br>• Drones de combat indigènes<br>• Guerre cyber avancée<br>• Systèmes hypersoniques</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Recommandations finales
        st.markdown("""
        <div class="nuclear-card">
            <h4>🎖️ RECOMMANDATIONS STRATÉGIQUES FINALES</h4>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-top: 1rem;">
                <div>
                    <h5>🛡️ DÉFENSE ACTIVE</h5>
                    <p>• Accélérer Make in India Défense<br>
                    • Renforcer la triade nucléaire<br>
                    • Développer les capacités cyber<br>
                    • Moderniser les forces conventionnelles</p>
                </div>
                <div>
                    <h5>🤝 COOPÉRATION STRATÉGIQUE</h5>
                    <p>• Approfondir le partenariat QUAD<br>
                    • Renforcer les relations avec la France<br>
                    • Développer la coopération indo-pacifique<br>
                    • Maintenir le partenariat avec la Russie</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Lancement du dashboard avancé
if __name__ == "__main__":
    dashboard = DefenseIndeDashboardAvance()
    dashboard.run_advanced_dashboard()