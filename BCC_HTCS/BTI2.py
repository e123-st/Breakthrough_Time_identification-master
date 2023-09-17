def BTTC() :
    import numpy as np
    import pandas as pd
    from kneed import KneeLocator
    import os
    import sys
    import gc    
        
    #建立储存文件夹
    G=[]
          
    #建立文件夹
    file_OUTPUT=os.path.exists('OUTPUT')
    file_FIGURE=os.path.exists('FIGURE')
    file_DATA=os.path.exists('DATA')

    if file_OUTPUT == False :
       os.mkdir('OUTPUT')
       
    if file_FIGURE == False :   
       os.mkdir('FIGURE')
       
    if file_DATA == False :
       os.mkdir('DATA')    

            
    #检测input文件
    file_input=os.path.exists('Parameters.input')
    if file_input==False:
       print('Warning:The "Parameters.input" does not exist.')
       G.append('Warning:The "Parameters.input" does not exist.')
       filename_input_Warning1 = "Input_Error.txt" 
       output_input_Warning1=open(r'OUTPUT/%s'%(filename_input_Warning1),'w')
       for l in range(len(G)):
           output_input_Warning1.write(str(G[l]))
           #output_input_Warning1.write("\t")#空4个字符 可以不加
           output_input_Warning1.write("\n")#\n换行
       output_input_Warning1.close()
       sys.exit(0) #终止程序    
            
    #从input文件导入参数
    input=open(r'Parameters.input','r')

    input1=input.readlines() #读取全部行

    G.append('Input Parameters')
    G.append('----------------------------------------------------------------------')
    G.append('Universal Parameters ')
    G.append('--------------------------------------------------')

    print('Input Parameters')
    print('----------------------------------------------------------------------')
    print('Universal Parameters ')
    print('--------------------------------------------------')

    IO=input1[0].replace('Address of Excel','') 
    IO=IO.strip() #删除空格
    if IO !='':
       print('Address of Excel : ',IO)
    IO_output='Address of Excel : ' + IO
    G.append(IO_output)


    sheet=input1[1].replace('sheet_name','') 
    sheet=sheet.strip() 
    if sheet != '' :
       print('sheet_name : ',sheet)
    sheet_name_output='sheet name : ' + sheet
    G.append(sheet_name_output)

    k=input1[2].replace('Row of Excel Table','')
    k=k.strip() 
    if k != '' :
       print('Row of Excel Table : ',k)
    k_output='Row of Excel Table : ' + k
    G.append(k_output)

    dz=input1[3].replace('Space Step Length [m]','')
    dz=dz.strip() 
    if dz != '' :
       print('Space Step Length [m] : ',dz)
    dz_output='Space Step Length [m] : ' + dz
    G.append(dz_output)
    if 'e' in dz :
        dz=dz.replace('e','*10**(')
        dz=dz + ')'
    if 'E' in dz :
        dz=dz.replace('E','*10**(')
        dz=dz + ')'


    Z=input1[4].replace('Space Steps','')
    Z=Z.strip()
    if Z != '' :
       print('Space Steps : ',Z)
    Z_output='Space Steps : ' + Z
    G.append(Z_output)
    if 'e' in Z :
        Z=Z.replace('e','*10**(')
        Z=Z + ')'
    if 'E' in Z :
        Z=Z.replace('E','*10**(')
        Z=Z + ')'


    dt=input1[5].replace('Time Step Length [h]','')
    dt=dt.strip() 
    if dt != '' :
       print('Time Step Length [h] : ',dt)
    dt_output='Time Step Length [h] : ' + dt
    G.append(dt_output)
    if 'e' in dt :
        dt=dt.replace('e','*10**(')
        dt=dt + ')'
    if 'E' in dt :
        dt=dt.replace('E','*10**(')
        dt=dt + ')'


    T_first=input1[6].replace('(minimum) Time Steps','')
    T_first=T_first.strip() 
    if T_first != '' :
       print('Minimum Time Steps : ',T_first)
    T_first_output='Minimum Time Steps : ' + T_first
    G.append(T_first_output)
    if 'e' in T_first :
        T_first=T_first.replace('e','*10**(')
        T_first=T_first + ')'
    if 'E' in T_first :
        T_first=T_first.replace('E','*10**(')
        T_first=T_first + ')'


    vs=input1[7].replace('Interstitial Velocity [m/s]','')
    vs=vs.strip()
    if vs != '' :
       print('Interstitial Velocity [m/s] : ',vs)
    vs_output='Interstitial Velocity [m/s] : ' + vs
    G.append(vs_output)
    if 'e' in vs :
        vs=vs.replace('e','*10**(')
        vs=vs + ')'
    if 'E' in vs :
        vs=vs.replace('E','*10**(')
        vs=vs + ')'


    P=input1[8].replace('Pressure [Pa]','')
    P=P.strip()
    if P != '' :
       print('Pressure [Pa] : ',P)
    P_output='Pressure [Pa] : ' + P
    G.append(P_output)
    if 'e' in P :
        P=P.replace('e','*10**(')
        P=P + ')'
    if 'E' in P :
        P=P.replace('E','*10**(')
        P=P + ')'

       
    T0=input1[9].replace('Temperature [K]','')
    T0=T0.strip()
    if T0 != '' :
       print('Temperature [K] : ',T0)
    T0_output='Temperature [K] : ' + T0
    G.append(T0_output)
    if 'e' in T0 :
        T0=T0.replace('e','*10**(')
        T0=T0 + ')'
    if 'E' in T0 :
        T0=T0.replace('E','*10**(')
        T0=T0 + ')'


    eb=input1[10].replace('Porosity of the Bed','')
    eb=eb.strip()
    if eb != '' :
       print('Porosity of the Bed : ',eb)
    eb_output='Porosity of the Bed : ' + eb
    G.append(eb_output)
    if 'e' in eb :
        eb=eb.replace('e','*10**(')
        eb=eb + ')'
    if 'E' in eb :
        eb=eb.replace('E','*10**(')
        eb=eb + ')'


    ep=input1[11].replace('Porosity of the Adsorbent Particles','')
    ep=ep.strip()
    if ep != '' :
       print('Porosity of the Adsorbent Particles : ',ep)
    ep_output='Porosity of the Adsorbent Particles : ' + ep
    G.append(ep_output)
    if 'e' in ep :
        ep=ep.replace('e','*10**(')
        ep=ep + ')'
    if 'E' in ep :
        ep=ep.replace('E','*10**(')
        ep=ep + ')'


    BTTC=input1[12].replace('Breakthrough Time Calculation','')
    BTTC=BTTC.strip()
    if BTTC != '' :
       print('Breakthrough time calculation : ',BTTC)
    BTTC_output='Breakthrough Time Calculation : ' + BTTC
    G.append(BTTC_output)    

    max_iteration=input1[13].replace('Maximum Iteration','')
    max_iteration=max_iteration.strip()
    mi_output='Maximum Iteration : '+str(max_iteration)
    print('Maximum Iteration : ',max_iteration)
    G.append(mi_output)    

    line_numbers=len(input1)
    n_c=0
    for i in np.arange(14,line_numbers):
        if 'Component' in input1[i] :
            n_c=n_c+1
    

    for i in np.arange(14,line_numbers):
        for component in np.arange(0,n_c):
            component_no='Component '+str(component)
            if component_no in input1[i]:
               globals()['name_'+str(component)]=input1[i].replace(component_no,'')
               globals()['name_'+str(component)]=globals()['name_'+str(component)].strip()
               globals()['y_'+str(component)]=input1[i+1].replace('molar fraction','')
               globals()['y_'+str(component)]=globals()['y_'+str(component)].strip()
               print('')
               component_name_output='Component '+str(component)+' : '+str(globals()['name_'+str(component)])
               print(component_name_output) 
               molar_fraction_output='molar fraction : '+str(globals()['y_'+str(component)])
               print(molar_fraction_output) 
               G.append('') 
               G.append(component_name_output)
               G.append(molar_fraction_output)
                  
               #转换为可计算   
               if 'e' in globals()['y_'+str(component)] :
                  globals()['y_'+str(component)]=globals()['y_'+str(component)].replace('e','*10**(')
                  globals()['y_'+str(component)]=globals()['y_'+str(component)] + ')'
               if 'E' in globals()['y_'+str(component)] :
                  globals()['y_'+str(component)]=globals()['y_'+str(component)].replace('E','*10**(')
                  globals()['y_'+str(component)]=globals()['y_'+str(component)] + ')'
               if globals()['y_'+str(component)] == '' : #不输入则为0
                  globals()['y_'+str(component)] = 0

               globals()['DL_'+str(component)+'_S']=input1[i+2].strip('axial dispersion cofficient [m^2/s]')
               globals()['DL_'+str(component)+'_S']=globals()['DL_'+str(component)+'_S'].strip()           
               axial_dispersion_cofficient_output='axial dispersion cofficient [m^2/s] : '+str(globals()['DL_'+str(component)+'_S'])
               print(axial_dispersion_cofficient_output)
               G.append(axial_dispersion_cofficient_output)
               #转换为可计算
               if 'e' in globals()['DL_'+str(component)+'_S'] :
                  globals()['DL_'+str(component)+'_S']=globals()['DL_'+str(component)+'_S'].replace('e','*10**(')
                  globals()['DL_'+str(component)+'_S']=globals()['DL_'+str(component)+'_S'] + ')'
               if 'E' in globals()['DL_'+str(component)+'_S'] :
                  globals()['DL_'+str(component)+'_S']=globals()['DL_'+str(component)+'_S'].replace('E','*10**(')
                  globals()['DL_'+str(component)+'_S']=globals()['DL_'+str(component)+'_S'] + ')'
               if globals()['DL_'+str(component)+'_S'] == '':
                  globals()['DL_'+str(component)+'_S'] = 0

    G.append('')   

    input.close

        
    #检查input文件是否存在所有参数
    if IO=='' or sheet=='' or k=='' or dz=='' or Z=='' or dt=='' or T_first=='' or vs=='' or P=='' or T0=='' or eb=='' or ep=='' or BTTC=='' :    
       print('Warning:Invalid parameters, please check.')
       G.append('Warning:Invalid parameters, please check.')
       filename_input_Warning2 = "Input_Error.txt" 
       output_input_Warning2=open(r'OUTPUT/%s'%(filename_input_Warning2),'w')
       for l in range(len(G)):
           output_input_Warning2.write(str(G[l]))
           #output_input_Warning2.write("\t")#空4个字符 可以不加
           output_input_Warning2.write("\n")#\n换行
       output_input_Warning2.close()
       sys.exit() #终止程序       
        
    for component in np.arange(0,n_c):
        if globals()['y_'+str(component)] != 0 :
           if globals()['DL_'+str(component)+'_S'] == 0 :
              print('Warning:Invalid parameters, please check.') 
              if 'Warning:Invalid parameters, please check.' not in G:      
                 G.append('Warning:Invalid parameters, please check.')
              filename_input_Warning2 = "Input_Error.txt" 
              output_input_Warning2=open(r'OUTPUT/%s'%(filename_input_Warning2),'w')
              for l in range(len(G)):
                  output_input_Warning2.write(str(G[l]))
                  #output_input_Warning2.write("\t")#空4个字符 可以不加
                  output_input_Warning2.write("\n")#\n换行
              output_input_Warning2.close()
              sys.exit() #终止程序 

    G.append('Parameters for Adsorbent')
    G.append('--------------------------------------------------')

    
    if BTTC=='No' :
       print('Warning:This is the setting for breakthrough curves calculation without the calculation of breakthrough times.')
       Material_output='Material : ' + str(globals()['name_'+str(component)])
       if Material_output not in G:   
          G.append(Material_output)#OUTPUT编号
          
       G.append('')
       
       if "Warning:This is the setting for breakthrough curves calculation without the calculation of breakthrough times." not in G:
          G.append('Warning:This is the setting for breakthrough curves calculation without the calculation of breakthrough times.')
       
       print('Finish')
       print('--------------------------------------------------')
       filename_time_error1 = "OUTPUT_" + str(globals()['name_'+str(component)]) + ".txt"
       output_time_error1=open(r'OUTPUT/%s'%(filename_time_error1),'w')#带有变量，字符中带有变量，‘%s'%(变量)
       for l in range(len(G)):
           output_time_error1.write(str(G[l]))
           #output_time_error1.write("\t")
           output_time_error1.write("\n")
       output_time_error1.close()
       sys.exit() #终止程序

    print('')
    print('Parameters for Adsorbent')
    print('--------------------------------------------------') 

    #固定系数 
    #时间单位：h 空间单位：m
    dz=eval(dz) #空间步长 eval()转换文字为运算 使用float()无法输入科学计数法的内容
    Z=int(eval(Z)) #空间步数 #固定床长L=dz*Z
    L=dz*Z
    dt=eval(dt) #时间步长 时间t=T*dt
    T_first=int(eval(T_first))#初始时间步数
    vs=eval(vs) 
    v=vs*3600 #间隙速度
    eb=eval(eb) #床层孔隙率
    ep=eval(ep) #颗粒孔隙率


    #总压 温度
    P=eval(P)
    R=8.314
    T0=eval(T0) #298K


    #各组分摩尔分数 & 进料浓度 & 加速识别阈值（10%C0）& 轴向扩散系数
    for component in np.arange(0,n_c) :
        globals()['y_'+str(component)]=eval(str(globals()['y_'+str(component)]))
        globals()['C_'+str(component)+'_0']=globals()['y_'+str(component)]*P/(R*T0)
        globals()['C_'+str(component)+'_10']=0.1*globals()['C_'+str(component)+'_0']
        globals()['DL_'+str(component)+'_S']=eval(str(globals()['DL_'+str(component)+'_S']))
        globals()['DL_'+str(component)]=3600*globals()['DL_'+str(component)+'_S']


    #导入数据
    #第二行为0行
    k=int(k)

    table = pd.read_excel(io=r''+IO,sheet_name=int(sheet))#表格从0算起 加r防转义

    #编号或名字
    No_or_Name=table.iloc[k,0]#先转换为字符串才可以判断是否为数字
    No_or_Name=str(No_or_Name)
    No=No_or_Name.isnumeric()
    if No==True:
       No_or_Name=int(No_or_Name)
       print('No or Name : ',No_or_Name)
    if No==False:
       print('No or Name : ',No_or_Name)         

      
    #材料及气体参数
    Pc=table.iloc[k,1]#材料的密度
    Pcnan=np.isnan(Pc)
    if Pcnan == False:
       print('Density of Material [kg/m^3] : ',Pc)  
       Pc_output='Density of Material [kg/m^3] : '+str(Pc)
       G.append(Pc_output)
       
    Pb=Pc*(1-eb)*(1-ep)#床层密度
    Pbnan=np.isnan(Pb)
    if Pbnan == False:
       print('Density of Bed [kg/m^3] : ',Pb) 
       Pb_output='Density of Bed [kg/m^3] : '+str(Pb)
       G.append(Pb_output)
      
    Ps=Pc*(1-ep)#颗粒密度
    Psnan=np.isnan(Ps)
    if Psnan == False:
       print('Density of Particle [kg/m^3] : ',Ps)
       Ps_output='Density of Particle [kg/m^3] : '+str(Ps)
       G.append(Ps_output)
        
    #饱和吸附量
    G.append('')
    G.append('Saturation Value of Adsorbate Loading [mol/kg]')
    print('Saturation Value of Adsorbate Loading [mol/kg]')

    for component in np.arange(0,n_c):
        globals()['qm_'+str(component)]=table.iloc[k,2+component]
        globals()['qm_'+str(component)+'_nan']=np.isnan(globals()['qm_'+str(component)])
        if globals()['qm_'+str(component)+'_nan'] == False and globals()['y_'+str(component)] != 0:
           globals()['qm_'+str(component)+'_output'] = 'Component '+str(component)+' : '+str(globals()['qm_'+str(component)])
           print(globals()['qm_'+str(component)+'_output']) 
           G.append(globals()['qm_'+str(component)+'_output'])
        if globals()['qm_'+str(component)+'_nan']==True and globals()['y_'+str(component)] != 0:
           globals()['qm_'+str(component)+'_output'] = 'Component '+str(component)+' : ' 
           print(globals()['qm_'+str(component)+'_output'])  
           G.append(globals()['qm_'+str(component)+'_output'])
        if globals()['qm_'+str(component)+'_nan']==True :   
           globals()['qm_'+str(component)]=0 
                  
    #朗缪尔系数
    G.append('')
    G.append('Equilibrium Constant of Langmuir [m^3/mol]')
    print('Equilibrium Constant of Langmuir [m^3/mol]')

    for component in np.arange(0,n_c):
        globals()['b_'+str(component)]=table.iloc[k,2+n_c+component]
        globals()['b_'+str(component)+'_nan']=np.isnan(globals()['qm_'+str(component)])
        if globals()['b_'+str(component)+'_nan'] == False and globals()['y_'+str(component)] != 0:
           globals()['b_'+str(component)+'_output'] = 'Component '+str(component)+' : '+str(globals()['b_'+str(component)])
           print(globals()['b_'+str(component)+'_output']) 
           G.append(globals()['b_'+str(component)+'_output'])
        if globals()['b_'+str(component)+'_nan']==True and globals()['y_'+str(component)] != 0:
           globals()['b_'+str(component)+'_output'] = 'Component '+str(component)+' : ' 
           print(globals()['b_'+str(component)+'_output'])  
           G.append(globals()['b_'+str(component)+'_output'])
        if globals()['b_'+str(component)+'_nan']==True :
           globals()['b_'+str(component)]=0

    #传质系数
    G.append('')
    G.append('Overall Mass Transfer Coefficient [s^-1]')
    print('Overall Mass Transfer Coefficient [s^-1]')

    for component in np.arange(0,n_c):
        if globals()['b_'+str(component)] == 0 :
           globals()['K_'+str(component)+'_s']=0
           globals()['K_'+str(component)+'_s_nan']=np.isnan(globals()['K_'+str(component)+'_s'])           
        if globals()['b_'+str(component)] != 0 :
           globals()['K_'+str(component)+'_s']=table.iloc[k,2+2*n_c+component]
           globals()['K_'+str(component)+'_s_nan']=np.isnan(globals()['K_'+str(component)+'_s'])
        if globals()['K_'+str(component)+'_s']!=0 and globals()['K_'+str(component)+'_s_nan']==False and globals()['y_'+str(component)] != 0: 
           globals()['K_'+str(component)+'_output']='Component '+str(component)+' : '+str(globals()['K_'+str(component)+'_s'])
           print(globals()['K_'+str(component)+'_output'])  
           G.append(globals()['K_'+str(component)+'_output'])
        if globals()['K_'+str(component)+'_s']==0 and globals()['K_'+str(component)+'_s_nan']==False and globals()['y_'+str(component)] != 0:   
           globals()['K_'+str(component)+'_output']='Component '+str(component)+' : '+'inf'
           print(globals()['K_'+str(component)+'_output'])  
           G.append(globals()['K_'+str(component)+'_output'])
        if globals()['K_'+str(component)+'_s_nan']==True and globals()['y_'+str(component)] != 0:
           globals()['K_'+str(component)+'_output']='Component '+str(component)+' : '
           print(globals()['K_'+str(component)+'_output']) 
           G.append(globals()['K_'+str(component)+'_output'])
        if globals()['K_'+str(component)+'_s_nan']==True :   
           globals()['K_'+str(component)+'_s']=0
           
    G.append('')
    G.append('Simulation Finish')
    G.append('----------------------------------------------------------------------')
    G.append('')


    #检查EXCEL
    filename_input_Warning3 = "Excel_Error.txt" 
    for component in np.arange(0,n_c):
        if globals()['y_'+str(component)] != 0:
           if globals()['qm_'+str(component)+'_nan']==True or globals()['b_'+str(component)+'_nan']==True or globals()['K_'+str(component)+'_s_nan']==True :
              print('Warning:Invalid parameters in excel table, please check.')
              Material_output='Material : ' + str(No_or_Name)
              if Material_output not in G:   
                 G.append(Material_output)#OUTPUT编   
              G.append('')
              G.append('Warning:Invalid parameters for component A in excel table, please check.')      
              output_input_Warning3=open(r'OUTPUT/%s'%(filename_input_Warning3),'w')
              for l in range(len(G)):
                  output_input_Warning3.write(str(G[l]))
                  #output_input_Warning3.write("\t")#空4个字符 可以不加
                  output_input_Warning3.write("\n")#\n换行
              output_input_Warning3.close()
              sys.exit() #终止程序
              
    #准备计算 & 换时间单位为h
    for component in np.arange(0,n_c):
        globals()['K_'+str(component)]=globals()['K_'+str(component)+'_s']*3600

    for iteration in np.arange(1,eval(max_iteration)+1) :  
        T=int(iteration*T_first)
        print('')
        print('Iteration : ',iteration)
        
    #建立网格
        for component in np.arange(0,n_c):
            globals()['C_'+str(component)]=np.zeros([Z+1,T+1])
            globals()['q_'+str(component)]=np.zeros([Z+1,T+1])
            
        #检测bug
        t=T*dt   
        space_time=np.arange(0,(T+1)*dt,dt)#不包括最后一个数
        max_time=np.max(space_time)
        if max_time>t:
           space_time=space_time[0:T+1] #去除由于python的BUG多出的数

        #收敛检测
        cmax=P/(R*T0)
        #print(cmax)

        print('--------------------------------------------------')
        print('Begin to calculate')
        print('--------------------------------------------------')
        
    #边界条件
        for j in np.arange(1,T+1):
            for component in np.arange(0,n_c):
                globals()['C_'+str(component)][0,j]=globals()['C_'+str(component)+'_0']
                globals()['q_'+str(component)][Z,j]=0
                globals()['q_'+str(component)][0,j]=0
    #初始条件
        for i in np.arange(0,Z+1):
            for component in np.arange(0,n_c):
                globals()['C_'+str(component)][i,0]=0
                globals()['q_'+str(component)][i,0]=0

        def sum_bc() :
            bc=0
            for component_no in np.arange(0,n_c) :
                bc=bc+globals()['b_'+str(component_no)]*globals()['C_'+str(component_no)][i,j]
                #print(component_no)
            return bc
        
    #递推关系
        for j in np.arange(0,T):
            #print(j)
            for i in np.arange(1,Z):
                #print(i)
                for component in np.arange(0,n_c):
                    #print(component)
                    B_C=sum_bc()
                    
                    globals()['C_'+str(component)][i,j+1]=dt*(((globals()['DL_'+str(component)]/(dz**2))+v/dz)*globals()['C_'+str(component)][i-1,j]+(1/dt-v/dz-(2*globals()['DL_'+str(component)])/(dz**2))*globals()['C_'+str(component)][i,j]+(globals()['DL_'+str(component)]/(dz**2))*globals()['C_'+str(component)][i+1,j]
                                     -(Ps*((1-eb)/eb)*globals()['K_'+str(component)]*(((globals()['b_'+str(component)]*globals()['qm_'+str(component)]*globals()['C_'+str(component)][i,j])/(1+B_C))-globals()['q_'+str(component)][i,j])))
                    
                    if globals()['b_'+str(component)] != 0:
                       globals()['q_'+str(component)][i,j+1]=globals()['K_'+str(component)]*dt*(((globals()['b_'+str(component)]*globals()['qm_'+str(component)]*globals()['C_'+str(component)][i,j])/(1+B_C))-globals()['q_'+str(component)][i,j])+globals()['q_'+str(component)][i,j]
                   
        #自测不收敛提前中止  
                    globals()['C_'+str(component)+'_nan']=np.isnan(globals()['C_'+str(component)][i,j+1])
                
                    if globals()['C_'+str(component)][i,j+1]> cmax or globals()['C_'+str(component)+'_nan'] ==True or globals()['q_'+str(component)][i,j+1] < 0 :
                       break 
                                
            for i in np.arange(Z,Z+1):
                for component in np.arange(0,n_c):
                    globals()['C_'+str(component)][i,j+1]=globals()['C_'+str(component)][i-1,j+1]
                   
        #自测不收敛提前中止
                    globals()['C_'+str(component)+'_nan']=np.isnan(globals()['C_'+str(component)][i,j+1])
               
                    if globals()['C_'+str(component)][i,j+1]> cmax or globals()['C_'+str(component)+'_nan'] ==True or globals()['q_'+str(component)][i,j+1] < 0 :
                       break        

        print('Finish')
        print('--------------------------------------------------')
        print('Begin to identify the breakthrough times')                
        print('--------------------------------------------------')
        
    #计算突破时间
        for component_10 in np.arange(0,n_c) :                  
            for t_10 in np.arange(0,T+1):
                C = globals()['C_'+str(component_10)][Z,t_10]
                globals()['dC_'+str(component_10)] = C - globals()['C_'+str(component_10)+'_10']
                if globals()['dC_'+str(component_10)] >= 0 :
                   globals()['t_'+str(component_10)] = t_10                      
                   break #中止运行循环 continue表示跳过条件，继续运行
                if t_10==T and globals()['dC_'+str(component_10)]<0 : 
                   print_10='Warning : please set larger Time Steps for Component ' + str(component_10)
                   print(print_10)
#                   for component_no in np.arange(0,n_c) :
#                       del globals()['C_'+str(component_10)]
#                       del globals()['q_'+str(component_10)]
#                   del space_time
#                   gc.collect()
#                   gc.DEBUG_UNCOLLECTABLE
#                   del gc.garbage[:] 
                   if iteration == max_iteration :
                      print('Warning : the setting of max_iteration and minimum Time step may be not long enough.Please check.')                      
                      print('Finish')
                      Material_output='Material : ' + str(No_or_Name)
                      if Material_output not in G:   
                         G.append(Material_output)#OUTPUT编号                        
                         G.append('')                    
                         if 'Warning : the setting of max_iteration and minimum Time step may be not long enough.Please check.' not in G:         
                            G.append('Warning : the setting of max_iteration and minimum Time step may be not long enough.Please check.')

        n_p=0             
        for component in np.arange(0,n_c) :                                                                               
            if globals()['dC_'+str(component)]>=0 : 
               n_p=n_p+1
        
        if n_p==n_c:
#导出结果
           Material_output='Material : ' + str(No_or_Name)
           if Material_output not in G:   
              G.append(Material_output)#OUTPUT编号
       #OUTPUT编号
           G.append('') 
           iteration_output='Iteration : '+str(iteration)
           G.append(iteration_output)
           G.append('') 

           for component in np.arange(0,n_c) : 
               
               globals()['x_'+str(component)]=space_time[0:globals()['t_'+str(component)]] 
               globals()['y_'+str(component)]=globals()['C_'+str(component)][Z,0:globals()['t_'+str(component)]] 
               globals()['KNEE_'+str(component)]=KneeLocator(globals()['x_'+str(component)],globals()['y_'+str(component)],curve='convex',direction='increasing',online=False)
               print('Component_',component)
               print('[h] : ',globals()['KNEE_'+str(component)].elbow)      
               print('[min] : ',globals()['KNEE_'+str(component)].elbow*60)
               print('[s] : ',globals()['KNEE_'+str(component)].elbow*3600)
               print('C/C0 for Breakthrough Time : ',(globals()['KNEE_'+str(component)].elbow_y)/(globals()['C_'+str(component)+'_0']))
               print('')
               globals()['component_'+str(component)+'_OUTPUT']='Component '+str(component)+' : ' + str(globals()['name_'+str(component)])
               globals()['T_'+str(component)+'_output_h'] = 'Breakthrough Time [h] : ' + str(globals()['KNEE_'+str(component)].elbow)
               globals()['T_'+str(component)+'_output_min'] = '                [min] : ' + str(globals()['KNEE_'+str(component)].elbow*60)
               globals()['T_'+str(component)+'_output_s'] = '                  [s] : ' + str(globals()['KNEE_'+str(component)].elbow*3600)
               globals()['c_'+str(component)+'c_'+str(component)+'_0_output'] = 'C/C0 for Breakthrough Time : ' + str((globals()['KNEE_'+str(component)].elbow_y)/(globals()['C_'+str(component)+'_0']))
                  
               if globals()['T_'+str(component)+'_output_h'] and globals()['T_'+str(component)+'_output_min'] and globals()['T_'+str(component)+'_output_s'] not in G :
                  G.append(globals()['component_'+str(component)+'_OUTPUT']) 
                  G.append(globals()['T_'+str(component)+'_output_h'])
                  G.append(globals()['T_'+str(component)+'_output_min'])
                  G.append(globals()['T_'+str(component)+'_output_s'])
               if globals()['c_'+str(component)+'c_'+str(component)+'_0_output'] not in G:
                  G.append('')  
                  G.append(globals()['c_'+str(component)+'c_'+str(component)+'_0_output'])
                  G.append('')
                
           break
                                                                               
    filename_time_output = "OUTPUT_" + str(No_or_Name) + ".txt"
    output_time_output=open(r'OUTPUT/%s'%(filename_time_output),'w')#带有变量，字符中带有变量，‘%s'%(变量)
    for l in range(len(G)):
        output_time_output.write(str(G[l]))
        #output_time_output.write("\t")
        output_time_output.write("\n")
    output_time_output.close()                 

    print('--------------------------------------------------')
    print('Finish')
               
    return print('--------------------------------------------------')
    

if __name__ == "__main__" :
   BTTC() #import时不会被启用
    
    

 
          

         
             

      
