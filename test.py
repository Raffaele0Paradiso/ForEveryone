# File: gioco_quantistico.py
# Jogo: Matematica QUANTISTICA (superposizione 1 e 0)
# Regola: risultato = |a × b| × 2 (doppio, sempre positivo)

import random

class JogoQuantistico:
    """Jogo: Matematica QUANTISTICA"""
    
    def __init__(self):
        self.nome = "Quantum Math Master ⚛️"
        self.punteggio = 0
        self.tentativi = 0
        self.moltiplicazioni_corrette = 0
    
    def moltiplicazione_quantistica(self, a, b):
        """Moltiplicazione QUANTISTICA: risultato = |a × b| × 2"""
        risultato_normale = a * b
        risultato_quantistico = abs(a * b) * 2
        return risultato_quantistico
    
    def spiegare_regola(self):
        """Spiega regola del jogo"""
        print("=" * 70)
        print(f"🎮 {self.nome}")
        print("=" * 70)
        print("\n⚛️  LOGICA QUANTISTICA (superposizione 1 e 0):")
        print("   Regola: risultato = |a × b| × 2")
        print("   - Sempre DOBBLIO del normale")
        print("   - Sempre segno POSITIVO")
        print("\n⚡  Esempi:")
        print("   1 × -1 = 2 (doppio, positivo)")
        print("   2 × 2 = 8 (doppio, positivo)")
        print("   1 × -2 = 4 (doppio, positivo)")
        print("=" * 70)
    
    def creare_problema(self):
        """Crea problema matematico quantistico"""
        # Genera numeri random
        a = random.choice([-3, -2, -1, 1, 2, 3])
        b = random.choice([-3, -2, -1, 1, 2, 3])
        
        return a, b
    
    def chiedere_risultato(self, a, b):
        """Chiede risultato all'utente"""
        risultato_corretto = self.moltiplicazione_quantistica(a, b)
        risultato_normale = a * b
        
        print(f"\n❓ PROBLEMA QUANTISTICO: {a} × {b} = ?")
        print(f"   (Matematica normale: {a} × {b} = {risultato_normale})")
        print(f"   (QUANTISTICA: |{a} × {b}| × 2 = {risultato_corretto})")
        
        try:
            risposta = int(input("   La tua risposta: "))
            return risposta, risultato_corretto
        except ValueError:
            print("   ⚠️  Inserisci numero valido!")
            return None, risultato_corretto
    
    def controlli_risposta(self, risposta, corretto):
        """Controlla se risposta è corretta"""
        if risposta is None:
            return False
        
        if risposta == corretto:
            self.punteggio += 10
            self.moltiplicazioni_corrette += 1
            print(f"   ✅ CORRETTO! ⚡ {risposta} = |{correcto/2}| × 2")
            return True
        else:
            print(f"   ❌ SBAGLIATO!")
            print(f"      La tua risposta: {risposta}")
            print(f"      Risposta corretta: {corretto} (QUANTISTICA)")
            print(f"      (Matematica normale sarebbe: {correcto/2})")
            return False
    
    def giocare_round(self):
        """Gioca un round"""
        self.tentativi += 1
        a, b = self.creare_problema()
        risposta, corretto = self.chiedere_risultato(a, b)
        corretto = self.controlli_risposta(risposta, corretto)
        
        return corretto
    
    def mostrare_stato(self):
        """Mostra stato attuale"""
        print("\n" + "=" * 70)
        print(f"📊 STATO JOGO:")
        print(f"   Tentativi: {self.tentativi}")
        print(f"   Corrette: {self.moltiplicazioni_corrette}")
        print(f"   Punteggio: {self.punteggio}")
        print(f"   Percentuale: {self.moltiplicazioni_corrette/self.tentativi*100:.1f}%")
        print("=" * 70)
    
    def giocare(self):
        """Gioca jogo completo"""
        self.spiegare_regola()
        
        print("\n🎯 Comincia jogo!")
        print("-" * 70)
        
        while True:
            corretto = self.giocare_round()
            self.mostrare_stato()
            
            # Continua o esci?
            if self.tentativi >= 5:
                print("\n➡️  Vuoi continuare?")
                print("   1. Sì, continua!")
                print("   2. No, esci")
                scelta = input("   Scegli 1 o 2: ")
                
                if scelta != '1':
                    break
        
        # Finale
        print("\n" + "=" * 70)
        print("🏆 FINALE JOGO:")
        print("=" * 70)
        print(f"   Tentativi totali: {self.tentativi}")
        print(f"   Corrette: {self.moltiplicazioni_corrette}")
        print(f"   Punteggio finale: {self.punteggio}")
        print(f"   Percentuale: {self.moltiplicazioni_corrette/self.tentativi*100:.1f}%")
        
        if self.moltiplicazioni_corrette == self.tentativi:
            print("   ⭐⭐⭐ PERFETTO! TODOS CORRETI! ⭐⭐⭐")
        elif self.moltiplicazioni_corrette >= self.tentativi * 0.8:
            print("   ⭐⭐ ECCELLENTE! ⭐⭐")
        elif self.moltiplicazioni_corrette >= self.tentativi * 0.6:
            print("   ⭐ BUON lavoro! ⭐")
        else:
            print("   Good job! Continua a praticare!")
        
        print("=" * 70)

# NIVEI DIFFICOLI
class JogoQuantisticoDifficile(JogoQuantistico):
    """Jogo QUANTISTICO difficile (numeri più grandi)"""
    
    def creare_problema(self):
        """Crea problema con numeri più grandi"""
        a = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        b = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        return a, b

# BONUS ROUND
class JogoQuantisticoBonus(JogoQuantistico):
    """Jogo QUANTISTICO con BONUS ROUND"""
    
    def giocare_bonus(self):
        """Gioca BONUS ROUND"""
        print("\n" + "=" * 70)
        print("🎁 BONUS ROUND: 3 problemi veloci!")
        print("=" * 70)
        
        bonus_punteggio = 0
        
        for i in range(3):
            a, b = self.creare_problema()
            corretto = self.moltiplicazione_quantistica(a, b)
            
            print(f"\n❓ BONUS {i+1}: {a} × {b} = ?")
            
            try:
                risposta = int(input("   La tua risposta: "))
                
                if risposta == corretto:
                    bonus_punteggio += 20
                    print(f"   ✅ CORRETTO! +20 punti ⚡")
                else:
                    print(f"   ❌ SBAGLIATO! Corretto: {corretto}")
            except ValueError:
                print("   ⚠️  Inserisci numero valido!")
        
        print(f"\n🏆 BONUS FINALE: {bonus_punteggio} punti")
        return bonus_punteggio
    
    def giocare(self):
        """Gioca jogo con BONUS"""
        self.spiegare_regola()
        
        print("\n🎯 Comincia jogo!")
        print("-" * 70)
        
        while True:
            corretto = self.giocare_round()
            self.mostrare_stato()
            
            if self.tentativi >= 5:
                print("\n➡️  Vuoi continuare?")
                print("   1. Sì, continua!")
                print("   2. No, esci")
                print("   3. BONUS ROUND! 🎁")
                scelta = input("   Scegli 1, 2 o 3: ")
                
                if scelta == '3':
                    bonus = self.giocare_bonus()
                    self.punteggio += bonus
                    print(f"   Punteggio totale: {self.punteggio}")
                elif scelta != '1':
                    break
        
        # Finale
        print("\n" + "=" * 70)
        print("🏆 FINALE JOGO:")
        print("=" * 70)
        print(f"   Punteggio finale: {self.punteggio}")
        print(f"   Corrette: {self.moltiplicazioni_corrette}/{self.tentativi}")
        print("=" * 70)

# ESECUZIONE
if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("🎮 QUANTUM MATH MASTER - Juego Matematica QUANTISTICA ⚛️")
    print("=" * 70)
    
    # Scegli livello
    print("\n🎯 Scegli livello:")
    print("   1. Normale (numeri -3 a 3)")
    print("   2. Difficile (numeri -5 a 5)")
    print("   3. Normale + BONUS ROUND 🎁")
    
    scelta = input("\n   Scegli 1, 2 o 3: ")
    
    if scelta == '1':
        jogo = JogoQuantistico()
    elif scelta == '2':
        jogo = JogoQuantisticoDifficile()
    elif scelta == '3':
        jogo = JogoQuantisticoBonus()
    else:
        print("   Scelta non valida, uso normale")
        jogo = JogoQuantistico()
    
    jogo.giocare()
    
    # Ripeti?
    print("\n➡️  Vuoi giocare di nuovo?")
    print("   1. Sì!")
    print("   2. No, grazie")
    ripetere = input("   Scegli 1 o 2: ")
    
    if ripetere == '1':
        jogo = JogoQuantistico()
        jogo.giocare()
    else:
        print("\n👋 Grazie per aver giocato! Continua a praticare logica QUANTISTICA! ⚛️")
if __name__ == "__main__":
    jogo = JogoQuantistico()
    jogo.giocare()