"actual proposal is below the first wall of text"
I'd like to make a platforming game in a metroidvania style including:
    * discrete rooms
    * non-linear map (which is to say, not just a sidescroller, a la the old Zelda games)
    * jump mechanic
    * focus on exploration rather than combat
*> Probably going to be a proof of concept (which is to say, "the mechanics are done but not the other stuff")
Main goals:
    Make a jumping mechanic
    * Scroll between windows smoothly
Main anti-goals:
    * Keep the mechanics down. Designing too many mechanics makes a game cluttered and messy. Simple >>>
    * mechanics => art every time it can look like crap so long as it works properly.
Extension goals:
    * Figure out a way to pick up items and have them change a mechanic (jump), changing the way the game is played.
    * etc

# Inspiration taken from http://store.steampowered.com/app/70300/VVVVVV/ which is an AMAZING game i highly recommend.

edited game prompt:
    * discrete rooms
    * non-linear map
    * jump mechanic
    * exploration, not combat. each room should aim to be a puzzle
Main goals:
    * make a jumping mechanic
    * figure out a way to jump off walls

### Linebreak!

Project: metroidvania with focus on exploration, a la VVVVVV, see above.
First major milestone: 
                    figuring out a jump mechanic, most likely using a flat acceleration and a gradual deceleration
                    based on the amount of time that has passed since the last time the player touched the ground
Things I don't know that I'll need to learn: 
                    figuring out how pygame tests for collision
                    basically the entirety of pygame itself to be honest
                    figuring out how pygame tests going offscreen and use that to change screens
Too ambitious:
                    mostly just a personal style of work but:
                        i'll end up trying to do too many things at once
                        getting the actual collision to work will be an issue and a half 
                        and is the reason why jumping is honestly the hardest thing to do in this game
not ambitious enough:
                    if jumping is a lot easier than i've thought then i have more mechanics to introduce planned but honestly
                    this entire section should be blank
                    


##Week 1: Spring Break Progress:
* didn't get much done this week. finished setting up git & did some testing to make sure that it works.
* pushed out stuff to github and set up a timeframe:
* Jump mechanic : end week 1 soft deadline, weekend 1 hard deadline.
* Jumping onto objects (collision): week 2 soft deadline, weekend 2 hard deadline.
* Changing between screens: week 3 soft deadline, weekend 3 hard deadline.
* Picking up items / art: week 4 soft deadline, weekend 4 hard deadline.
Game is designed to be a tech demo, art can wait / can be done given time at the end of the project.

* Considered how to do the jump mechanic, tossed around ideas.
    * concept 1: jump velocity is a certain amount but for every second that the player is off the ground (not colliding with object) downwards accel increase.
        issue: requires collision to get working.
        looked up some things on pygame collision, bookmarked & saved.
    * concept 2: jump velocity is just a U but upside down - track out each bit of the jump (aka track out going up & the jump curve, going down & curve, hovering in between)
        issue: lot of busy work for little gain.
