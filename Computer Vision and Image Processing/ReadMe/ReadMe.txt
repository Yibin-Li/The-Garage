1.make sure intall 
2.pip install opencv, matplotlib, numpy
3.change the picture range in the python file: generate_coordinates.py
4.run generate_coordinates.py
5.line 125: waitKey means the waiting time when displaying each picture
	    the bigger the value waitKey taking in, 
	    the longer it displays each picture


6.In most cases, you don't need to change the value of any variable; 
  Each colored circle tracks a labled point;
  Follow the colored circle to make sure what does each circle track:
	Here is all the lables we are tracking:
		left_front_wheel, left_back_wheel, left_armor
		right_front_wheel, right_back_wheel, right_armor
		front, back
	Here is a summary of the correspondence of colored circle:
		left_red: white circle
		right_red: pink_green circle
		orange: blue circle
		left_blue: red circle
		right_blue: green circle
   What do you need to do: 
		open the coordinates.csv, change left_red, right_red, orange, left_blue, right_blue to the corresponding lable location
		whenver the circle tracks a different lable location, you should enter a new line to indicate
		look up the example.csv to see the what should the final csv be like

7.Handle some really special cases that no colored circle is tracking certain lable:
	Possible reasons: 1. the size of min_area
			  2. the bound of colors
	Handle case1: change the value of variable min_area
	Handle case2: 
			1. use showpic.py to open the target picture
			2. get the bgr value of the point(when you run the showpic.py, you will see two pictures, 
			   the left one can show you the bgr value of each pixel)
                        3. open gethsv.py, enter the bgr value you get in the 'target' variale
			4. run gethsv.py
			5. replace the lower and upper bound in generate_coordinates.py, 
			   The last two values of the bound mean 'brightness', you can change the lower_bound [..., 100, 100] to [..., 155, 155]
			   to narrow the searching range if the circle is not tracking the labled point you want.

