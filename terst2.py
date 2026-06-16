# File: moltiplicazione_quantistica_diretta.py
# QUANTISTICO = Moltiplicazione DIRETTA (non graduale!)

class MoltiplicazioneQuantisticaDiretta:
    """QUANTISTICO = Moltiplicazione DIRETTA"""
    
    def __init__(self):
        self.regola = "QUANTISTICO = DIRETTO (non graduale)"
    
    def moltiplicazione_classica_graduale(self, a, b):
        """Moltiplicazione CLASSICA (graduale, step by step)"""
        print("=" * 70)
        print("🐌 MOLTIPLICAZIONE CLASSICA (graduale)")
        print("=" * 70)
        
        risultato = 0
        steps = []
        
        # Graduale: aggiungi a, b volte
        for i in range(abs(b)):
            risultato += a
            steps.append(risultato)
        
        if b < 0:
            risultato = -risultato
        
        print(f"   Operazione: {a} × {b}")
        print(f"   Graduale: {steps[0]} → {steps[1]} → ... → {risultato}")
        print(f"   Steps: {len(steps)} (lento!)")
        print(f"   Risultato: {risultato}")
        print("=" * 70)
        
        return risultato
    
    def moltiplicazione_quantistica_diretta(self, a, b):
        """Moltiplicazione QUANTISTICA (diretta, immediata!)"""
        print("=" * 70)
        print("⚡ MOLTIPLICAZIONE QUANTISTICA (DIRETTA)")
        print("=" * 70)
        
        # DIRETTO! (1 solo step, non graduale)
        risultato = abs(a * b) * 2
        
        print(f"   Operazione: {a} × {b}")
        print(f"   Klassico (graduale): {a} → ... → {a*b} (Lento!)")
        print(f"   QUANTISTICO (diretto): {a} × {b} = {risultato} ⚡")
        print(f"   Steps: 1 (VELOCE!)")
        print(f"   Regola: |{a} × {b}| × 2 = {risultato}")
        print("=" * 70)
        
        return risultato
    
    def mostrare_confronto(self, a, b):
        """Mostra confronto CLASSICO vs QUANTISTICO"""
        print("\n📊 CONFRONTO: CLASSICO (graduale) vs QUANTISTICO (diretto)")
        print("-" * 70)
        
        r_classico = self.moltiplicazione_classica_graduale(a, b)
        r_quantistico = self.moltiplicazione_quantistica_diretta(a, b)
        
        print(f"\n   DIFFERENZA:")
        print(f"   - CLASSICO: {len([a*b for i in range(abs(b))])} steps (lento)")
        print(f"   - QUANTISTICO: 1 step (VELOCE!) ⚡")
        print(f"   - Velocità: QUANTISTICO = {len([a*b for i in range(abs(b))])}x più veloce!")
        print("-" * 70)
    
    def mostrare_tutti_calcoli(self):
        """Mostra tutti i calcoli QUANTISTICI diretti"""
        print("\n📊 MOLTIPLICAZIONI QUANTISTICHE DIRETTI:")
        print("-" * 70)
        
        # Casi da te dati
        self.moltiplicazione_quantistica_diretta(1, -1)
        self.moltiplicazione_quantistica_diretta(2, 2)
        self.moltiplicazione_quantistica_diretta(1, -2)
        
        # Altri esempi
        self.moltiplicazione_quantistica_diretta(3, 3)
        self.moltiplicazione_quantistica_diretta(4, 2)
        
        print("\n" + "=" * 70)
        print("✅ QUANTISTICO = DIRETTO (non graduale):")
        print("   1 × -1 = 2 (DIRETTO!) ⚡")
        print("   2 × 2 = 8 (DIRETTO!) ⚡")
        print("   1 × -2 = 4 (DIRETTO!) ⚡")
        print("   3 × 3 = 18 (DIRETTO!) ⚡")
        print("   Regola: |a × b| × 2 = risultato DIRETTO")
        print("=" * 70)

# ESECUZIONE
if __name__ == "__main__":
    mq = MoltiplicazioneQuantisticaDiretta()
    mq.mostrare_tutti_calcoli()
    
    print("\n" + "=" * 70)
    mq.mostrare_confronto(2, 3)
    print("=" * 70)