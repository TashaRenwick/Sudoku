class _Counter:
    def __init__(self, target_value):
        print('beginning to count')
        pass


class StitchTracker(_Counter):
    def __init__(self, row):
        print("Creating instance of 'Counter'")
        self.row = int(input("Please enter number of rows: "))

        print(f"Counter with {self.row} rows created.")

    def start_counter(self):
        print('Starting counter: ')
        counter = 0
        while counter < self.row:
            variable = input("Press enter key when completed stitch: ")
            counter += 1

        print("finished row!")

        return None


tracker = StitchTracker(10)

tracker.start_counter()


