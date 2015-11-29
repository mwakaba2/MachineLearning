'''
Background:

In 1973, the University of California-Berkeley (UC-Berkeley) was sued for sex discrimination. Its admission data showed that men applying to graduate school at UC-Berkley were more likely to be admitted than women.

The graduate schools had just accepted 44% of male applicants but only 35% of female applicants. The difference was so great that it was unlikely to be due to chance.

By looking at the data more closely, you may realize that there is more to the story than meets the eye.


Data:

Why don't you download the 1973 UC-Berkeley Graduate School Admission Data and take a look yourself. This dataset contains information about the six most popular departments.

Feel free to examine and analyze the data with you favorite tool, like Excel, R, or even pen and paper.


Question for you:

Now, do you agree that UC-Berkeley discriminated against women during the admission process?

No because when you examine the admittance rate for each Department, the admission rate is actually higher for women than men.
Since there are a lot more men applying than women in the first place, a lot more men are likely to be admitted out of the pool.


What do other experts say?:

Once you have made a decision, see if you came to the same conclusion as other experts.

Don't worry if you didn't arrive at the same conclusion! This is a tricky exercise on a topic otherwise known as Simpson's Paradox.

Hope you had fun! Now Dave will tell you about other type problems that you can use data science to analyze.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


''' Analyze the admitted rate for each gender in each department '''
data = pd.read_csv('Berkeley.csv')
male_df = data[data.Gender == 'Male']
female_df = data[data.Gender == 'Female']
admitted_fs = []
admitted_ms = []


def admitted_percentage(df, dept):
	dept_df = df[df.Dept == dept]
	dept_total = float(dept_df.sum()['Freq'])
	dept_admitted = float(dept_df[dept_df.Admit == 'Admitted'].sum()['Freq'])
	dept_score = dept_admitted / dept_total
	return dept_score

'''Department A Statistics'''
m_a_score = admitted_percentage(male_df, 'A')
f_a_score = admitted_percentage(female_df, 'A')

admitted_ms.append(m_a_score)
admitted_fs.append(f_a_score)

'''Department B Statistics'''
m_b_score = admitted_percentage(male_df, 'B')
f_b_score = admitted_percentage(female_df, 'B')

admitted_ms.append(m_b_score)
admitted_fs.append(f_b_score)

'''Department C Statistics'''
m_c_score = admitted_percentage(male_df, 'C')
f_c_score = admitted_percentage(female_df, 'C')

admitted_ms.append(m_c_score)
admitted_fs.append(f_c_score)

'''Department D Statistics'''
m_d_score = admitted_percentage(male_df, 'D')
f_d_score = admitted_percentage(female_df, 'D')

admitted_ms.append(m_d_score)
admitted_fs.append(f_d_score)

'''Department E Statistics'''
m_e_score = admitted_percentage(male_df, 'E')
f_e_score = admitted_percentage(female_df, 'E')

admitted_ms.append(m_e_score)
admitted_fs.append(f_e_score)

'''Department F Statistics'''
m_f_score = admitted_percentage(male_df, 'F')
f_f_score = admitted_percentage(female_df, 'F')

admitted_ms.append(m_f_score)
admitted_fs.append(f_f_score)

''' Scale rate to percentage '''
admitted_ms = [ 100 * rate for rate in admitted_ms ]
admitted_fs = [ 100 * rate for rate in admitted_fs ]

''' Plot results '''
# the x locations for the departments
ind = np.arange(6) 
width = 0.35

fig, ax = plt.subplots()
female = ax.bar(ind, tuple(admitted_fs), width, color='r')
male = ax.bar(ind+width, tuple(admitted_ms), width, color='b')

# adding some text for labels, titles and axes ticks
ax.set_ylabel('Admittance Rate')
ax.set_title('Admittance rate by Department and Gender')
ax.set_xticks(ind+width)
ax.set_xticklabels(('DeptA', 'DeptB', 'DeptC', 'DeptD', 'DeptE', 'DeptF'))
ax.legend((female, male), ('Female', 'Male'))
ax.set_ylim([0, 100])

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(male)
autolabel(female)

plt.show()