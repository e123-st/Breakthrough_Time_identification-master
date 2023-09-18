from BCC_HTCS.BCC import Breakthrough_times_output,DATA_output,Figure_output

Breakthrough_times_output()

DATA_output(unit_of_time='h')

Figure_output(unit_of_time='h',
              save_figure='No',
              save_type='tif',
              dpi=100,
              linestyle_A='-',
              linestyle_B='-',
              linestyle_C='-',
              linestyle_D='-',
              linecolor_A='b',
              linecolor_B='r',
              linecolor_C='g',
              linecolor_D='y',
              plotmarker_A='^',
              plotmarker_B='^',
              plotmarker_C='^',
              plotmarker_D='^',
              plotcolor_A='b',
              plotcolor_B='r',
              plotcolor_C='g',
              plotcolor_D='y')


