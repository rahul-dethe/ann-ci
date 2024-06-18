import pstats
import sys

def filter_profile(input_file, script_name):
    p = pstats.Stats(input_file)
    # p.strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE)
    # p.strip_dirs().sort_stats(pstats.SortKey.TIME)
    p.strip_dirs().sort_stats(pstats.SortKey.TIME).print_stats(script_name)
    
    # Create a new Stats object for filtered data
    # filtered_stats = pstats.Stats()
    
    # for func, stat in p.stats.items():
    #     if script_name in func[0]:
    #         filtered_stats.stats[func] = stat
    #         print(stat)
    
    # Dump the filtered stats to a file
    # filtered_stats.dump_stats(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python filter_profile.py <input_file> <output_file> <script_name>")
        sys.exit(1)

    input_file = sys.argv[1]
    script_name = sys.argv[2]
    
    filter_profile(input_file, script_name)

