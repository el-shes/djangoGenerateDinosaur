import django
django.setup()

from generate_dino.models import Dino


def lines_in_file_to_db(file_path):
    """ Handles reading lines from a file and saving to the Database.

    :param file_path: Path to where file is located.
    :type file_path: str
    """

    with open(file_path) as file:
        f = file.readlines()
        for line in f:
            Dino.objects.create(name=line)


if __name__ == "__main__":
    lines_in_file_to_db('dinosaur-names.txt')
