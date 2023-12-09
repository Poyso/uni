# Insiemi

#### Teorema degli Insiemi
Tutto in matematica e un insieme\
I concetti primitivi della matematica sono:
- insieme
- elemento
- appartenenze
Un insieme e un gruppo di oggetti, elementi appartenenti all insieme

$Insieme = [ elemento1, elemento2 .... ]$\
E.g $[2,7,3]$
- Un insieme puo essere elemento di un altro Insieme\
E.g $[1,3,[1,2],[1,2,3]]$
- In un insieme l ordine non conta\
E.g $[1,2,3] = [1,3,2]$
- In un insieme non ci possono essere ripetizioni\
E.g $[1,2,2]$ non e un insieme

#### Gli insiemi sono:

- N=numeri non negativi $[1,2,3,4....n]$
- P=numeri positivi $[0,1,2,3,4...n]$
- Z=numeri non positivi $[...,-4,-3,-2,-1,0]$
- Q=numeri razionali $[-1/2,0,1/3,1/2....n]$

Se $a \in N$ allora
$[a]=[1,2,3,4....a]$
Scriviamo:
$A=[....]
A e l insieme definito da $[....]$
$x \in A$ per dire x appartiene ad A
$x non\in A$ per dire x appartiene ad A
L insieme che non ha elementi si dice insieme vuoto => /o
/o=[]

#### Operazioni tra insiemi
A,B sono insiemi

- Def: L intersezione tra A e B crea un altro insieme\
$A \cap B = [x \in A : x \in B]$\
(':' <=> tali che)
- Def: L unione di A e B ha come elementi di A e di B\
$A \cup B$\
$A \cup /o=A$\
$A \cap /o=/o$
- Def B e un sottoinsieme di A (incluso)\
$B \subseteq A$ se ogni elemento di B e' anche elemento di A
- Oss: A,B,C insiemi. Se A e' sottoinsieme di B e B e' sottoinsieme di C, allora A e' sottoinsieme di C\
$A \subseteq B$ e $B \subseteq C$ => $A \subseteq C$
- Def: 2 insiemi sono uguali se hanno gli stessi elementi\
$A=B$
Oss: $A=B$ => $B \subseteq A$ e $A \subseteq B$

#### Proprieta
A,B,C

##### Proprieta associative
$A \cup(B \cup C)=(A \cup B) \cup C$\
$A \cap(B \cap C)=(A \cap B) \cap C$\

##### Proprieta disertive
$A \cup (B \cap C)=(A \cup B) \cap (A \cup C)$\
$A \cap (B \cup C)=(A \cap B) \cup (A \cap C)$\

###### Dimostrazione
$A \cup (B \cap C) \subseteq (A \cup B) \cap (A \cup C)$\

$x \in A \cup (B \cap C)$ => $x \in A$ or $x \in B \cap C$\
se $x A \cup B$ allora $x \in A \cup C$

Viceversa dimostriamo che\
$(A \cup B) \cap (A \cup C) \subseteq A \cup (B \cap C)$\
$x \in (A \cup B) \cap (A \cup C)$ => $x \in A \cup B$ e $x \in A \cup C$\
se $x \in A$ => $x \in A \cup (B \cup C)$

- Def: tutti gli insiemi e sotto insiemi sono sottoinsiemi di un grande insieme (U)\
- Def: A insieme, il complementare di A e' l insieme $A' = [x \in U : x !\in A]$\
#### Leggi di de Morgan
A,B insiemi

$(A \cup B)'=A' \cap B'$
$(A \cap B)'=A' \cup B'$
