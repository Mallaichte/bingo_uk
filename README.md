# bingo_uk
Generates UK standard bingo books (6 tickets to a page, numbers 1-90), generates and calls numbers for game, and checks claims.

## Blah blah narrative
My first proper job (I don't count the part-time Christmas job at Toys 'R' Us that I had when I was in high school) was in a bingo hall. I started in the booksales department and I remember a light-hearted argument with the supervisor and a member of staff that included the retort "How would you know? Do you know what an RNG looks like? How would you know if it's simple!?". RNG wasn't a term in common-use outside the gaming industries (both gambling and video-gaming), and in bingo halls it had almost mystical connotations. This was in 2002 and I'd just finished my Highers. I listened thinking "Well an RNG is simple to code - at least in corel. There's a function built-in for it."
"Ah! But how do you know the built-in function is random enough to meet the standards required for bingo? Remember that random isn't really random!" I answered myself back.
"Fair point. Well, I've still got VB6. I'll try making an RNG for bingo when I go home."

I did try, but something you should know is that the term RNG meant more than just the number generation when used in the bingo. We meant the program that generated the numbers AND validated claims - among other things. I started with something "simple" though. The actual random number generator. So randomly generate numbers from 1-90 90 times. "Oh! Obviously, we'll have duplicates to deal with! Don't worry. We'll just reject those and keep trying until we get a number that hasn't been generated already."

**Yes! Really!** I *really* thought that was a good idea. After several minutes staring at the screen, it inevitably threw up an error. It took weeks before it occurred to me to populate a list and remove the numbers from the list as I go. I never finished all the other stuff that goes under the banner of "RNG", so I'm going back to that now, but for the actual RNG the Python random module will suffice for this project. What's included and planned in this current project is listed further down. As for back then, I'm really glad I kept my mouth shut while listening to that argument. An experience that has served me well in the years since.

There is a feature of bingo tickets (at least UK ones) that I had forgotten until I printed one off for testing. When looking over it I could see it was off and immediately recognised why. Although the numbers on a page should be random, the numbers on a column within an individual ticket should be sorted. For any columns with more than one number on a ticket (3 rows and 9 columns with 5 numbers to a row remember [4 blank]), the numbers can be sorted without fear of giving too much order to the numbers on the page. As long as the blank cells remain in place, it shouldn't cause any issues.

This project isn't for any real-life uses, it's just a personal challenge for skills practice and education. However, I will try and build upon it more and more to simulate its real-life counterparts. That means the ability to create multiple books and multiple pages to a book. Calling a game will require players to be working from the correct book and page, which will also be validated when checking claims. Speaking of validating claims, I also need to add a condition to check the last called number is on one of the completed lines. I've left that out for now so I can spam the call button then check tickets for testing. It will also include ticket pricing and a calculation for minimum legal prize payout and recommended payout with customisable rules (e.g. return a certain percent rounded to a certain number of significant figures). The option to manually set prizes or auto-set within the user set rules. On validation, prize money can be calculated for split claims (when more than one winning ticket is validated).

## Currently working
- [x] Generate pages of tickets (6 tickets to a page, 3 rows of 9 columns to a ticket [18 rows to a page], 5 unique numbers from 1-90 per row)
- [x] Print legible books to screen
- [x] Validate claims for line, double and house

## Currently being worked on
- [ ] sort order of numbers in columns within individual tickets (as described above)

## To be worked on
- [ ] Multi-page books
- [ ] Add condition to claim check to ensure last number called is on a completed line (currently omitted to simplify testing)
- [ ] Columns within individual tickets (not books) to be sorted
- [ ] Export books to alternative format to print hard copy (haven't decided best format yet)
- [ ] Prize money (minimum, recommended, setting, calculating split claims)
