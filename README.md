TheEleventhArchmage
===========
This is going to be an online CCG.

folder __pycache__: Compiled files.

folder BigYellowCactus...:Source code from Regnancy, a Python implementation of Dominion, which I'm using for inspiration.

folder iso: source code for isotropic's networking/server whatever, and I have no idea how it works.

folder tests: Test files I use to make sure I know what I'm doing before trying something in the main code.

file card: Has the Card class, and a class for each type of card.

file cardtest5: My current main file - run this to run the game itself.

file deck: Has the Deck class, which details methods for lists of Cards.

file deckaccess: Not currently in use - pickles input files and unpickles them - will use this to save decks that the player designs.

file frostcards: Contains the cards of the Frost sphere.

file game: Will eventually have methods detailing all the phases a player goes through during their turn.

file lightningcards: Contains the cards of the Lightning sphere.

file player: Contains the Player class, and methods related to it, like drawing cards or dealing damage to other players.



Rules:
Players come in with a deck of cards of various card types.  They draw 7 cards to start.
At the start of their turn, players may play a single Focus card, which gives focus in its sphere.
There are ten spheres: Frost, Fire, Glass, Silk, Metal, Lightning, Earth, Poison, Illusion, Blood
Each sphere has its flavor and unique abilities.

Once a player has focus in play to use, they may play other cards - as many as they like, as long as they have unused
focus.  Cards remain attached to focus until they are no longer in play.  

After playing cards, these cards are activated - their effects come into play, damage is dealt, etc.

Projectiles are discarded immediately after being activated, freeing up focus for next turn.

Creatures remain in play until they are killed by your oppponent's creature(s) or projectile(s).  

If your opponent has creatures in play, you have the option of targeting those creatures with your own creatures or
projectiles.  Doing so is generally a good idea, since creatures will continue to do damage while in play.  Or, you can
simply target your opponent directly, regardless of him having creatures.

Augments can be played on Projectiles to give them a special bonus for this turn, and are discarded upon activation, like
projectiles.

Effects (not implemented yet) remain in play indefinitely, like creatures, and provide some passive bonus while in play.

At the start of your turn you can choose to release creatures in order to free up focus for other cards - doing so 
discards these creatures, so they may not be played again.

If a player has no cards remaining in their deck when they go to draw a card at the start of their turn, or if they have
0 health at any point, they lose.  Last player remaining wins.

