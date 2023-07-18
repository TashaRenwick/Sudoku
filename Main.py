class Counter:
    def __init__(self, target_value):
        self.target_value = target_value

    def start_counter(self):
        counter = 0


class StitchTracker(Counter):
    def __init__(self, row):
        print("Creating instance of 'Tracker'")

        self.rows = int(input("Please enter number of rows: "))
        self.stitches = int(input("Please enter number of stitches in all rows: "))

        print(f"Tracker with {self.rows} rows and {self.stitches} stitches per row created.")

    def start_tracker(self):
        print('\n Starting tracker: ')

        # Creating variables that track number of rows + stitches
        counter_rows = 0
        counter_stitch = 0

        while counter_rows < self.rows:
            print(f'\n Number of completed rows: {counter_rows}/{self.rows}')

            while counter_stitch < self.stitches:
                print(f'\n Number of completed stitches: {counter_stitch}/{self.stitches}')

                variable = input("Press the Enter key when completed stitch: ")
                counter_stitch += 1

            print(f'\n Number of completed stitches: {counter_stitch}/{self.stitches}')
            print("Finished row!")

            counter_rows += 1
            counter_stitch = 0      # This is where having a counter class would be useful, can just create another instance



        return None


tracker = StitchTracker(10)

tracker.start_tracker()


