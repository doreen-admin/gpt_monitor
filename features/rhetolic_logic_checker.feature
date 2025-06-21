Feature: Rhetolic Logic Checker

    Background:
        Given Assistant Instructions of Rhetolic and Logic Checker

    Scenario: Make a query to Rhetolic and Logic Checker
        When User asks the Assistant a Query of Lacan's text
        Then the Reply contains reference to Lacan
        And the Reply contains reference to determinis(m|t)
        And the Reply contains reference to metaphor
        And the Reply contains reference to mathematic
        And the Reply contains reference to psychoanaly(sis|tic|st)

    Scenario: Make a query to Rhetolic and Logic Checker
        When User asks the Assistant a Query of Trump's tweet
        Then the Reply contains reference to ad hominem
        And the Reply contains reference to appeal to fear
        And the Reply contains reference to false dilemma
        And the Reply contains reference to slippery slope
        And the Reply contains reference to due process
        And the Reply contains reference to partisan
        And the Reply contains reference to stigmatiz(e|ing)
        And the Reply contains reference to oversimplif(y|ication)

    Scenario: Make a query to Rhetolic and Logic Checker
        When User asks the Assistant a Query of transparent white
        Then the Reply contains reference to nuance
        And the Reply contains reference to ambigu(ous|ity)
        And the Reply contains reference to (translucen(t|cy)|partial|frosted)

    Scenario: Make a query to Rhetolic and Logic Checker
        When User asks the Assistant a Query of DHMO
        Then the Reply contains reference to water
        And the Reply contains reference to correlation
        And the Reply contains reference to (benefi(t|cial)|fundamental)
        And the Reply contains reference to inconsisten(t|cy)
        And the Reply contains reference to mislead
        And the Reply contains reference to satir(e|ical)

    Scenario: Make a query to Rhetolic and Logic Checker
        When User asks the Assistant a Query of Jabberwocky
        Then the Reply contains reference to Jabberwocky
        And the Reply contains reference to nonsens(e|ical)
        And the Reply contains reference to poe(t|m)
