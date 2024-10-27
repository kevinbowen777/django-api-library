Add book list
=============

Template for adding a list of books to django-api-library Django application

.. code-block:: console

    book = Book.objects.create(
        title="",
        author="",
        isbn="",
    )

Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample book list
----------------

.. code-block:: console

    book = Book.objects.create(
        title="Brave New World",
        subtitle="",
        author="Aldous Huxley",
        isbn="0060929871",
    )

    Book.objects.create(
        title="Django for Beginners",
        subtitle="Learn web development with Django",
        author="William S. Vincent",
        isbn="1735467200",
    )

    Book.objects.create(
        title="Django for APIs",
        subtitle="Build web APIs with Python & Django",
        author="William S. Vincent",
        isbn="1093633948",
    )

    Book.objects.create(
        title="Django for Professionals",
        subtitle="Production websites with Python & Django",
        author="William S. Vincent",
        isbn="31735467235",
    )

    Book.objects.create(
        title="Atoms, Metaphors and Paradoxes",
        subtitle="Niels Bohr and the Construction of a New Physics",
        author="Sandro Petruccioli",
        isbn="0521031885",
    )

    Book.objects.create(
        title="Luce elettricità magnetismo",
        subtitle="",
        author="Sandro Petruccioli",
        isbn="9781234567897",
    )

    Book.objects.create(
        title="The Structure of Scientific Revolutions",
        subtitle="",
        author="Thomas Kuhn",
        isbn="0226458083",
    )

    Book.objects.create(
        title="Black-Body Theory and the Quantum Discontinuity, 1894-1912",
        subtitle="",
        author="Thomas Kuhn",
        isbn="0226458008",
    )

    Book.objects.create(
        title="Capitalist Realism",
        subtitle="Is There No Alternative?",
        author="Mark Fisher",
        isbn="1846943175",
    )

    Book.objects.create(
        title="Ghosts of My Life",
        subtitle="Writings on Depression, Hauntology and Lost Futures",
        author="Mark Fisher",
        isbn="1846253175",
    )

    Book.objects.create(
        title="The Conquest of Bread",
        subtitle="",
        author="Pyotr Kropotkin",
        isbn="1904859100",
    )

    Book.objects.create(
        title="Anarchism",
        subtitle="A Collection of Revolutionary Writings",
        author="Pyotr Kropotkin",
        isbn="978048641955",
    )

    Book.objects.create(
        title="My Mother: Demonology",
        subtitle="",
        author="Kathy Acker",
        isbn="0517144867",
    )

    Book.objects.create(
        title="Blood and Guts in High School",
        subtitle="",
        author="Kathy Acker",
        isbn="080213193X",
    )

    Book.objects.create(
        title="Dubliners",
        subtitle="",
        author="James Joyce",
        isbn="0192839993",
    )

    Book.objects.create(
        title="Ulysses",
        subtitle="",
        author="James Joyce",
        isbn="2132546652001",
    )

    Book.objects.create(
        title="Eyeless in Gaza",
        subtitle="",
        author="Aldous Huxley",
        isbn="0192828893",
    )

    Book.objects.create(
        title="Programming Python",
        subtitle="",
        author="Mark Lutz",
        isbn="0967144867",
    )

    Book.objects.create(
        title="Test-Driven Development with Python",
        subtitle="",
        author="Harry J.W. Percival",
        isbn="2317144867",
    )

    Book.objects.create(
        title="Two Scoops of Django 3.x",
        subtitle="",
        author="Daniel Feldroy",
        isbn="4917144867",
    )
