import pandas as pd
import matplotlib.pyplot as plt

# Define School Codes
BranciforteCode = 6060149
MissionHillCode =  6060156

# Read data files
County18DF = pd.read_csv('data_files/sb_ca2018_all_44_csv_v3.txt')
County17DF = pd.read_csv('data_files/sb_ca2017_all_44_csv_v2.txt')
County16DF = pd.read_csv('data_files/sb_ca2016_all_44_csv_v3.txt')
County15DF = pd.read_csv('data_files/sb_ca2015_all_44_csv_v3.txt')
groupsKey = pd.read_json('data_files/groups_key.json')["groupKeys"].to_dict() 

# Drop and/or ranme columns not consistent across all years
County16DF = County16DF.drop(columns=['Total CAASPP Enrollment']) 
County15DF = County15DF.drop(columns=['Total CAASPP Enrollment'])

RenameDict = {'Area 1 Percentage At or Near Standard':'Area 1 Percentage Near Standard',
              'Area 2 Percentage At or Near Standard':'Area 2 Percentage Near Standard',
              'Area 3 Percentage At or Near Standard':'Area 3 Percentage Near Standard',
              'Area 4 Percentage At or Near Standard':'Area 4 Percentage Near Standard',
              'Total Tested at Subgroup Level':'Total Tested with Scores'}
County15DF = County15DF.rename(columns=RenameDict)

# Concatenate all years
CountyDF = pd.concat([County18DF, County17DF, County16DF, County15DF ])

# Add groups description field
CountyDF['Student Groups'] = CountyDF['Subgroup ID'].map(lambda x: groupsKey[str(x)])  

# Permormance Index (PI) field
CountyDF['Area 1 PI'] = 5  \
                   + 2.5*CountyDF['Area 1 Percentage Near Standard'].str.replace('*','Inf').astype('float')/100.0 \
                   + 5*(CountyDF['Area 1 Percentage Above Standard'].str.replace('*','Inf').astype('float')/100.0 \
                          - CountyDF['Area 1 Percentage Below Standard'].str.replace('*','Inf').astype('float')/100.0)  

CountyDF['Area 2 PI'] = 5  \
                   + 2.5*CountyDF['Area 2 Percentage Near Standard'].str.replace('*','Inf').astype('float')/100.0 \
                   + 5*(CountyDF['Area 2 Percentage Above Standard'].str.replace('*','Inf').astype('float')/100.0 \
                          - CountyDF['Area 2 Percentage Below Standard'].str.replace('*','Inf').astype('float')/100.0) 

CountyDF['Area 3 PI'] = 5  \
                   + 2.5*CountyDF['Area 3 Percentage Near Standard'].str.replace('*','Inf').astype('float')/100.0 \
                   + 5*(CountyDF['Area 3 Percentage Above Standard'].str.replace('*','Inf').astype('float')/100.0 \
                          - CountyDF['Area 3 Percentage Below Standard'].str.replace('*','Inf').astype('float')/100.0)

CountyDF['Area 4 PI'] = 5  \
                   + 2.5*CountyDF['Area 4 Percentage Near Standard'].str.replace('*','Inf').astype('float')/100.0 \
                   + 5*(CountyDF['Area 4 Percentage Above Standard'].str.replace('*','Inf').astype('float')/100.0 \
                          - CountyDF['Area 4 Percentage Below Standard'].str.replace('*','Inf').astype('float')/100.0) 

# Select data for each school
BranciforteDF = CountyDF[CountyDF['School Code'] == BranciforteCode ]
MissionDF = CountyDF[CountyDF['School Code'] == MissionHillCode]

# Rname PI columns to distinguish between schools
RenameDict = {'Area 1 PI':'Branciforte Area 1 PI',
              'Area 2 PI':'Branciforte Area 2 PI',
              'Area 3 PI':'Branciforte Area 3 PI',
              'Area 4 PI':'Branciforte Area 4 PI'}
BranciforteDF = BranciforteDF.rename(columns=RenameDict)
            
RenameDict = {'Area 1 PI':'Mission Area 1 PI',
              'Area 2 PI':'Mission Area 2 PI',
              'Area 3 PI':'Mission Area 3 PI',
              'Area 4 PI':'Mission Area 4 PI'}
MissionDF = MissionDF.rename(columns=RenameDict)

# Select fields

#7th grade
BranciforteDF_7G_A1_PI = BranciforteDF[['Test Year', 'Student Groups', 'Branciforte Area 1 PI']][(BranciforteDF['Test Id']==1)  & (BranciforteDF['Grade']==7)]
BranciforteDF_7G_A2_PI = BranciforteDF[['Test Year', 'Student Groups', 'Branciforte Area 2 PI']][(BranciforteDF['Test Id']==1)  & (BranciforteDF['Grade']==7)]
BranciforteDF_7G_A3_PI = BranciforteDF[['Test Year', 'Student Groups', 'Branciforte Area 3 PI']][(BranciforteDF['Test Id']==1)  & (BranciforteDF['Grade']==7)]
BranciforteDF_7G_A4_PI = BranciforteDF[['Test Year', 'Student Groups', 'Branciforte Area 4 PI']][(BranciforteDF['Test Id']==1)  & (BranciforteDF['Grade']==7)]

MissionDF_7G_A1_PI = MissionDF[['Test Year', 'Student Groups', 'Mission Area 1 PI']][(MissionDF['Test Id']==1)  & (MissionDF['Grade']==7)]
MissionDF_7G_A2_PI = MissionDF[['Test Year', 'Student Groups', 'Mission Area 2 PI']][(MissionDF['Test Id']==1)  & (MissionDF['Grade']==7)]
MissionDF_7G_A3_PI = MissionDF[['Test Year', 'Student Groups', 'Mission Area 3 PI']][(MissionDF['Test Id']==1)  & (MissionDF['Grade']==7)]
MissionDF_7G_A4_PI = MissionDF[['Test Year', 'Student Groups', 'Mission Area 4 PI']][(MissionDF['Test Id']==1)  & (MissionDF['Grade']==7)]

# 8th grade
BranciforteDF_8G_A1_PI = BranciforteDF[['Test Year', 'Student Groups', 'Branciforte Area 1 PI']][(BranciforteDF['Test Id']==1)  & (BranciforteDF['Grade']==8)]
BranciforteDF_8G_A2_PI = BranciforteDF[['Test Year', 'Student Groups', 'Branciforte Area 2 PI']][(BranciforteDF['Test Id']==1)  & (BranciforteDF['Grade']==8)]
BranciforteDF_8G_A3_PI = BranciforteDF[['Test Year', 'Student Groups', 'Branciforte Area 3 PI']][(BranciforteDF['Test Id']==1)  & (BranciforteDF['Grade']==8)]
BranciforteDF_8G_A4_PI = BranciforteDF[['Test Year', 'Student Groups', 'Branciforte Area 4 PI']][(BranciforteDF['Test Id']==1)  & (BranciforteDF['Grade']==8)]

MissionDF_8G_A1_PI = MissionDF[['Test Year', 'Student Groups', 'Mission Area 1 PI']][(MissionDF['Test Id']==1)  & (MissionDF['Grade']==8)]
MissionDF_8G_A2_PI = MissionDF[['Test Year', 'Student Groups', 'Mission Area 2 PI']][(MissionDF['Test Id']==1)  & (MissionDF['Grade']==8)]
MissionDF_8G_A3_PI = MissionDF[['Test Year', 'Student Groups', 'Mission Area 3 PI']][(MissionDF['Test Id']==1)  & (MissionDF['Grade']==8)]
MissionDF_8G_A4_PI = MissionDF[['Test Year', 'Student Groups', 'Mission Area 4 PI']][(MissionDF['Test Id']==1)  & (MissionDF['Grade']==8)]

# 7th and 8th grade for distribution in subgroup analysis
BranciforteDF_Ntested = BranciforteDF[['Test Year', 'Student Groups', 'Total Tested with Scores']][(BranciforteDF['Test Id']==1) & (BranciforteDF['Grade']==8)] 
MissionDF_Ntested = MissionDF[['Test Year', 'Student Groups', 'Total Tested with Scores']][(MissionDF['Test Id']==1)  & (MissionDF['Grade']==8)]

# Make plots

# Time series plots
claims = ['A1', 'A2', 'A3', 'A4']
claim_titles = ['Reading', 'Writing', 'Listening', 'Research/Inquiry']
xticks = [2015, 2016, 2017, 2018]
xticks_labels = ['2015', '2016', '2017', '2018']

for i,claim in enumerate(claims):
    figure, axes = plt.subplots(1, 2, sharey=True)

    # Select group 1 (All) and index by year
    M7Selection =  eval('MissionDF_7G_'+claim+'_PI')[eval('MissionDF_7G_'+claim+'_PI')['Student Groups']=='All Students'].set_index('Test Year')
    B7Selection =  eval('BranciforteDF_7G_'+claim+'_PI')[eval('BranciforteDF_7G_'+claim+'_PI')['Student Groups']=='All Students'].set_index('Test Year')
    M8Selection =  eval('MissionDF_8G_'+claim+'_PI')[eval('MissionDF_8G_'+claim+'_PI')['Student Groups']=='All Students'].set_index('Test Year')
    B8Selection =  eval('BranciforteDF_8G_'+claim+'_PI')[eval('BranciforteDF_8G_'+claim+'_PI')['Student Groups']=='All Students'].set_index('Test Year')

    M7Selection = M7Selection.drop(columns=['Student Groups'])
    B7Selection = B7Selection.drop(columns=['Student Groups'])
    M8Selection = M8Selection.drop(columns=['Student Groups'])
    B8Selection = B8Selection.drop(columns=['Student Groups'])
    
    axes[0].plot(pd.concat([M7Selection, B7Selection], axis=1))
    axes[0].set_xticks(xticks)
    axes[0].set_xticklabels(xticks_labels)
    axes[0].set_title('7th Grade')
    axes[0].legend(['Mission', 'Branciforte'])
    
    axes[1].plot(pd.concat([M8Selection, B8Selection], axis=1))
    axes[1].set_xticks(xticks)
    axes[1].set_xticklabels(xticks_labels)
    axes[1].set_title('8th Grade')
    axes[1].legend(['Mission', 'Branciforte'])

    axes[0].set_ylabel('Performance Score', fontsize='16')
    figure.set_size_inches(10,5)
    figure.suptitle('Claim '+str(i+1)+': '+claim_titles[i])
    figure.savefig('figures/Claim'+str(i+1)+'_Allgroups.png')
    
plt.close('all')  

# Distribution plots
years = [2015, 2016, 2017, 2018]

# Score  across groups
for year in years:
    for i,claim in enumerate(claims):
        B8Selection = eval('BranciforteDF_8G_'+claim+'_PI')[eval('BranciforteDF_8G_'+claim+'_PI')['Test Year']==year].drop(columns=['Test Year']).set_index('Student Groups')
        M8Selection = eval('MissionDF_8G_'+claim+'_PI')[eval('MissionDF_8G_'+claim+'_PI')['Test Year']==year].drop(columns=['Test Year']).set_index('Student Groups')
        B8Selection =  B8Selection.dropna()
        M8Selection =  M8Selection.dropna()
        plotDF = pd.concat( [ M8Selection, B8Selection], axis = 1, sort=False)
        plotDF['Sort by'] = plotDF.max(axis=1)
        plotDF = plotDF.sort_values(by=['Sort by']).drop(columns=['Sort by'])
        plotDF = plotDF.rename(columns={plotDF.columns[0]:"Mission", plotDF.columns[1]:"Branciforte" })
        plot = plotDF.plot.barh(fontsize=15)
        plot.legend(prop={'size': 20})
        plot.axes.set_position([0.3,0.08, 0.68,0.85])
        plot.axes.set_ylabel('')
        plot.axes.set_xlabel('Performance Score', fontsize='20')
        plot.get_figure().set_size_inches(16,10)
        plot.get_figure().suptitle(str(year)+'     8th Grade      '+'Claim '+str(i+1)+': '+claim_titles[i]+'    Performance Scores', fontsize=20)
        plot.get_figure().savefig('figures/'+claim+'PIbyGroups_8G_'+str(year)+'.png') 
plt.close('all') 

        
for year in years:
    for i,claim in enumerate(claims):
        B7Selection = eval('BranciforteDF_7G_'+claim+'_PI')[eval('BranciforteDF_7G_'+claim+'_PI')['Test Year']==year].drop(columns=['Test Year']).set_index('Student Groups')
        M7Selection = eval('MissionDF_7G_'+claim+'_PI')[eval('MissionDF_7G_'+claim+'_PI')['Test Year']==year].drop(columns=['Test Year']).set_index('Student Groups')
        B7Selection =  B7Selection.dropna()
        M7Selection =  M7Selection.dropna()
        plotDF = pd.concat( [ M7Selection, B7Selection], axis = 1, sort=False)
        plotDF['Sort by'] = plotDF.max(axis=1)
        plotDF = plotDF.sort_values(by=['Sort by']).drop(columns=['Sort by'])
        plotDF = plotDF.rename(columns={plotDF.columns[0]:"Mission", plotDF.columns[1]:"Branciforte" })
        plot = plotDF.plot.barh(fontsize=15)
        plot.legend(prop={'size': 20})
        plot.axes.set_position([0.3,0.08, 0.68,0.85])
        plot.axes.set_ylabel('')
        plot.axes.set_xlabel('Performance Score', fontsize='20')
        plot.get_figure().set_size_inches(16,10)
        plot.get_figure().suptitle(str(year)+'     7th Grade      '+'Claim '+str(i+1)+': '+claim_titles[i]+'    Performance Scores', fontsize=20)
        plot.get_figure().savefig('figures/'+claim+'PIbyGroups_7G_'+str(year)+'.png') 
plt.close('all') 

# Number of students across groups
for year in years:
    BSelection = BranciforteDF_Ntested[BranciforteDF_Ntested['Test Year']==year].drop(columns=['Test Year']).set_index('Student Groups')
    MSelection = MissionDF_Ntested[MissionDF_Ntested['Test Year']==year].drop(columns=['Test Year']).set_index('Student Groups')
    BSelection = BSelection.mask(BSelection['Total Tested with Scores']=='*').dropna()
    MSelection = MSelection.mask(MSelection ['Total Tested with Scores']=='*').dropna()
    BSelection = BSelection.rename(columns={'Total Tested with Scores':'Branciforte Number of Students Tested'})
    MSelection = MSelection.rename(columns={'Total Tested with Scores':'Mission Number of Students Tested'})
    plotDF = pd.concat( [ MSelection.astype(int), BSelection.astype(int)], axis = 1, sort=False)
    plotDF['Sort by'] = plotDF.max(axis=1)
    plotDF = plotDF.sort_values(by=['Sort by']).drop(columns=['Sort by'])
    plotDF = plotDF.rename(columns={plotDF.columns[0]:"Mission", plotDF.columns[1]:"Branciforte" })
    plot = plotDF.plot.barh(fontsize=15)
    plot.legend(prop={'size': 20})
    plot.axes.set_position([0.3,0.08, 0.68,0.85])
    plot.axes.set_ylabel('')
    plot.axes.set_xlabel('Number of Students', fontsize='20')
    plot.get_figure().set_size_inches(16,10)
    plot.get_figure().suptitle(str(year)+'     Number of Students tested (7th and 8th Grade) ', fontsize=20)
    plot.get_figure().savefig('figures/'+'StudentsTestedByGroup'+str(year)+'.png') 
plt.close('all') 

