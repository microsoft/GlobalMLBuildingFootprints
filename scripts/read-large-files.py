
"""
This python script is an example of how to read a large file, line-delimited and split it into multiple
parts. This can be helpful when using a machine that cannot load an entire file into memory. 
"""
import os

def main():
    # path to decompressed geojsonl file
    input_file = "Angola.geojsonl"

    # check to make sure we can find the input file
    assert os.path.exists(input_file), f"{input_file} not found!"

    # template output file path. the script will populate the curly brackets {} with a number
    output_file_template = "Angola_part-{}.geojsonl"

    # this is the maximum number of features per file. adjust as desired. 10k features produces ~3MB files. 
    buildings_per_file = 10_000

    # open the large file
    with open(input_file) as inf:
        # read a single line
        line = inf.readline()

        # used for updating file numbers
        file_counter = 1

        # this is where we count the number of features in a single file
        lines_per_file = 0

        # create the actual file path fome the template above
        current_target_file_path = output_file_template.format(file_counter)

        # prevent overwriting existing files
        assert not os.path.exists(current_target_file_path), f"{current_target_file_path} already exists!"

        # open an output file in write mode. 
        target = open(current_target_file_path, 'w')
        
        # start iterating through each feature
        while line:

            # write a single feature to the current output files
            target.write(line)

            # increment the count for number of features in a file
            lines_per_file += 1

            # go to next feature in the large file
            line = inf.readline()

            # check if we have hit the desire feature limit per file
            if lines_per_file == buildings_per_file:
                # close the current target file since we've reached the desired feature limit
                target.close()
                print(f"wrote {lines_per_file:,} lines to {current_target_file_path}")

                # increment the file counter so we can create a new output
                file_counter += 1
                
                # reset the line counter for the new output file
                lines_per_file = 0 
            
                # create the path for the next output file
                current_target_file_path = output_file_template.format(file_counter)
                # prevent overwriting existing files
                assert not os.path.exists(current_target_file_path), f"{current_target_file_path} already exists!"
                
                # open the next output file
                target = open(current_target_file_path, 'w')

        # when we get here, there are no more features left in the larger file so we close the last target file
        if not target.closed:
            print(f"wrote {lines_per_file:,} lines to {current_target_file_path}")
            target.close()
    print(f"Complete!")


if __name__ == "__main__":
    main()
    