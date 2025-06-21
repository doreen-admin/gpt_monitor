Feature: Narrative Factory

    Background:
        Given Assistant Instructions of Narrative Factory

    Scenario: Make a query to Narrative Factory
        When User asks the Assistant a Query of Theodicy
        Then the Reply contains reference to free will
        And the Reply contains reference to spiritual (development|growth)
        And the Reply contains reference to (lack|privation)
        And the Reply contains reference to (dynamic|process)
        And the Reply contains reference to (unknown|infinite|mystery)
        And the Reply contains reference to atheis(m|t)

    Scenario: Make a query to Narrative Factory
        When User asks the Assistant a Query of Free will
        Then the Reply contains reference to (neuroscience|cognitive)
        And the Reply contains reference to (theolog(y|cal)|devine|god)
        And the Reply contains reference to quantum
        And the Reply contains reference to (illusion|fiction|determinis(m|t))
        And the Reply contains reference to compatib(le|ilist)

    Scenario: Make a query to Narrative Factory
        When User asks the Assistant a Query of Poverty
        Then the Reply contains reference to structural
        And the Reply contains reference to caste
        And the Reply contains reference to gender
        And the Reply contains reference to growth
        And the Reply contains reference to corrupt
        And the Reply contains reference to (education|training)
        And the Reply contains reference to (population|demographic)

    Scenario: Make a query to Narrative Factory
        When User asks the Assistant a Query of Accelerated aging
        Then the Reply contains reference to (effective|valid)
        And the Reply contains reference to limited
        And the Reply contains reference to observation
        And the Reply contains reference to compl(ex|icated)

    Scenario: Make a query to Narrative Factory
        When User asks the Assistant a Query of Flat earth
        Then the Reply contains reference to scien(ce|tific)
        And the Reply contains reference to oblate spheroid
        And the Reply contains reference to conspiracy
        And the Reply contains reference to flat earth

