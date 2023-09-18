def BTTC(type,max_iteration=5) :
    
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

    IO=input1[0].strip('Address of Excel') 
    IO=IO.strip() #删除空格
    if IO !='':
       print('Address of Excel : ',IO)
    IO_output='Address of Excel : ' + IO
    G.append(IO_output)


    sheet=input1[1].strip('sheet_name') 
    sheet=sheet.strip() 
    if sheet != '' :
       print('sheet_name : ',sheet)
    sheet_name_output='sheet name : ' + sheet
    G.append(sheet_name_output)

    k=input1[2].strip('Row of Excel Table')
    k=k.strip() 
    if k != '' :
       print('Row of Excel Table : ',k)
    k_output='Row of Excel Table : ' + k
    G.append(k_output)

    dz=input1[3].strip('Space Step Length [m]')
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


    Z=input1[4].strip('Space Steps')
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


    dt=input1[5].strip('Time Step Length [h]')
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


    T_first=input1[6].strip('Time Steps')
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


    vs=input1[7].strip('Interstitial Velocity [m/s]')
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


    P=input1[8].strip('Pressure [Pa]')
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

       
    T0=input1[9].strip('Temperature [K]')
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


    eb=input1[10].strip('Porosity of the Bed')
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


    ep=input1[11].strip('Porosity of the Adsorbent Particles')
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


    BTTC=input1[12].strip('Breakthrough Time Calculation')
    BTTC=BTTC.strip()
    if BTTC != '' :
       print('Breakthrough time calculation : ',BTTC)
    BTTC_output='Breakthrough Time Calculation : ' + BTTC
    G.append(BTTC_output)
   
    mi_output='Maximum Iteration : ' + str(max_iteration)
    print('Maximum Iteration : ',max_iteration)
    G.append(mi_output)

    A_name=input1[14].replace('Component A','')
    A_name=A_name.strip()

    yA=input1[15].strip('molar fraction')
    yA=yA.strip()
    if yA != 0 and yA != '':
       print('')
       print('Component A :', A_name) 
       print('molar fraction : ',yA) 
       G.append(' ') 
       A_name_output='Component A : '+ A_name
       G.append(A_name_output)
       yA_output='molar fraction : ' + yA
       G.append(yA_output)
    #转换为可计算   
    if 'e' in yA :
        yA=yA.replace('e','*10**(')
        yA=yA + ')'
    if 'E' in yA :
        yA=yA.replace('E','*10**(')
        yA=yA + ')'
    if yA == '' : #不输入则为0
       yA = 0

    DLAS=input1[16].strip('axial dispersion cofficient [m^2/s]')
    DLAS=DLAS.strip()
    if DLAS != '' :
       print('axial dispersion cofficient [m^2/s] : ',DLAS)
    if DLAS != 0 and DLAS != '':
       DLAS_output='axial dispersion cofficient [m^2/s] : ' + DLAS
       G.append(DLAS_output)
    #转换为可计算
    if 'e' in DLAS :
        DLAS=DLAS.replace('e','*10**(')
        DLAS=DLAS + ')'
    if 'E' in DLAS :
        DLAS=DLAS.replace('E','*10**(')
        DLAS=DLAS + ')'
    if DLAS == '':
       DLAS = 0


    B_name=input1[18].replace('Component B','')
    B_name=B_name.strip()

    yB=input1[19].strip('molar fraction')
    yB=yB.strip()   
    if yB != 0 and yB != '':
       print('') 
       print('Component B :', B_name)
       print('molar fraction : ',yB) 
       G.append(' ') 
       B_name_output='Component B : '+ B_name
       G.append(B_name_output)
       yB_output='molar fraction : ' + yB
       G.append(yB_output)
    #转换为可计算   
    if 'e' in yB :
        yB=yB.replace('e','*10**(')
        yB=yB + ')'
    if 'E' in yB :
        yB=yB.replace('E','*10**(')
        yB=yB + ')'
    if yB == '' : #不输入则为0
       yB = 0

    DLBS=input1[20].strip('axial dispersion cofficient [m^2/s]')
    DLBS=DLBS.strip()
    if DLBS != '' :
       print('axial dispersion cofficient [m^2/s] : ',DLBS)
    if DLBS != 0 and DLBS != '':
       DLBS_output='axial dispersion cofficient [m^2/s] : ' + DLBS
       G.append(DLBS_output)
    #转换为可计算
    if 'e' in DLBS :
        DLBS=DLBS.replace('e','*10**(')
        DLBS=DLBS + ')'
    if 'E' in DLBS :
        DLBS=DLBS.replace('E','*10**(')
        DLBS=DLBS + ')'
    if DLBS == '':
       DLBS = 0


    C_name=input1[22].replace('Component C','')
    C_name=C_name.strip()

    yC=input1[23].strip('molar fraction')
    yC=yC.strip()
    if yC != 0 and yC != '':
       print('') 
       print('Component C :', C_name) 
       print('molar fraction : ',yC) 
       G.append(' ') 
       C_name_output='Component C : '+ C_name
       G.append(C_name_output)
       yC_output='molar fraction : ' + yC
       G.append(yC_output)
    #转换为可计算   
    if 'e' in yC :
        yC=yC.replace('e','*10**(')
        yC=yC + ')'
    if 'E' in yC :
        yC=yC.replace('E','*10**(')
        yC=yC + ')'
    if yC == '' : #不输入则为0
       yC = 0

    DLCS=input1[24].strip('axial dispersion cofficient [m^2/s]')
    DLCS=DLCS.strip()
    if DLCS != '' :
       print('axial dispersion cofficient [m^2/s] : ',DLCS)
    if DLCS != 0 and DLCS != '':
       DLCS_output='axial dispersion cofficient [m^2/s] : ' + DLCS
       G.append(DLCS_output)
    #转换为可计算
    if 'e' in DLCS :
        DLCS=DLCS.replace('e','*10**(')
        DLCS=DLCS + ')'
    if 'E' in DLCS :
        DLCS=DLCS.replace('E','*10**(')
        DLCS=DLCS + ')'
    if DLCS == '':
       DLCS = 0


    D_name=input1[26].replace('Component D','')
    D_name=D_name.strip()

    yD=input1[27].strip('molar fraction')
    yD=yD.strip()
    if yD != 0 and yD != '':
       print('') 
       print('Component D :', D_name) 
       print('molar fraction : ',yD) 
       G.append(' ') 
       D_name_output='Component D : '+ D_name
       G.append(D_name_output)
       yD_output='molar fraction : ' + yD
       G.append(yD_output)
    #转换为可计算   
    if 'e' in yD :
        yD=yD.replace('e','*10**(')
        yD=yD + ')'
    if 'E' in yD :
        yD=yD.replace('E','*10**(')
        yD=yD + ')'
    if yD == '' : #不输入则为0
       yD = 0

    DLDS=input1[28].strip('axial dispersion cofficient [m^2/s]')
    DLDS=DLDS.strip()
    if DLDS != '' :
       print('axial dispersion cofficient [m^2/s] : ',DLDS)
    if DLDS != 0 and DLDS != '':
       DLDS_output='axial dispersion cofficient [m^2/s] : ' + DLDS
       G.append(DLDS_output)
    #转换为可计算
    if 'e' in DLDS :
        DLDS=DLDS.replace('e','*10**(')
        DLDS=DLDS + ')'
    if 'E' in DLDS :
        DLDS=DLDS.replace('E','*10**(')
        DLDS=DLDS + ')'
    if DLDS == '':
       DLDS = 0

    G.append(' ')   

    input.close
            
       
    #检查input文件是否存在所有参数
    y=yA+yB+yC+yD
    if IO=='' or sheet=='' or k=='' or dz=='' or Z=='' or dt=='' or T_first=='' or vs=='' or P=='' or T0=='' or eb=='' or ep=='' or BTTC=='' or y==0 :    
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

    if yA != 0 :
       if DLAS == 0 :
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

    if yB != 0 :
       if DLBS == 0 :
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
          
    if yC != 0 :
       if DLCS == 0 :
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

    if yD != 0 :
       if DLDS == 0 :
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


    #各组分摩尔分数
    yA=eval(str(yA))
    yB=eval(str(yB))
    yC=eval(str(yC))
    yD=eval(str(yD))


    #进料浓度
    CA_0=yA*P/(R*T0)
    CB_0=yB*P/(R*T0)
    CC_0=yC*P/(R*T0)
    CD_0=yD*P/(R*T0)


    #加速识别阈值（10%C0）
    CA_10=0.1*CA_0
    CB_10=0.1*CB_0
    CC_10=0.1*CC_0
    CD_10=0.1*CD_0


    #轴向扩散系数s
    DLAS=eval(str(DLAS))
    DLBS=eval(str(DLBS))
    DLCS=eval(str(DLCS))
    DLDS=eval(str(DLDS))

    #换单位为h
    DLA=DLAS*3600
    DLB=DLBS*3600
    DLC=DLCS*3600
    DLD=DLDS*3600


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
    G.append('Saturation Value of Adsorbate Loading [mol/kg]')
    print('Saturation Value of Adsorbate Loading [mol/kg]')

    qmA=table.iloc[k,2]
    qmAnan=np.isnan(qmA)
    if qmAnan == False and yA != 0:
       print('A : ', qmA) 
       qmA_output='A : '+str(qmA)
       G.append(qmA_output)
    if qmAnan==True and yA != 0:
       print('A : ')  
       qmA_output='A : '
       G.append(qmA_output)
    if qmAnan==True :   
       qmA=0
       
    qmB=table.iloc[k,3]
    qmBnan=np.isnan(qmB) 
    if qmBnan == False and yB != 0:
       print('B : ', qmB)  
       qmB_output='B : '+str(qmB)
       G.append(qmB_output)
    if qmBnan==True and yB != 0:
       print('B : ')  
       qmB_output='B : '
       G.append(qmB_output)
    if qmBnan==True :   
       qmB=0
       
    qmC=table.iloc[k,4]
    qmCnan=np.isnan(qmC)
    if qmCnan == False and yC != 0:
       print('C : ', qmC)  
       qmC_output='C : '+str(qmC)
       G.append(qmC_output)
    if qmCnan==True and yC != 0:
       print('C : ')  
       qmC_output='C : '
       G.append(qmC_output)
    if qmCnan==True :   
       qmC=0
       
    qmD=table.iloc[k,5]
    qmDnan=np.isnan(qmD)
    if qmDnan == False and yD != 0:
       print('D : ', qmD)  
       qmD_output='D : '+str(qmD)
       G.append(qmD_output)
    if qmDnan==True and yD != 0:
       print('D : ')  
       qmD_output='D : '
       G.append(qmD_output)
    if qmDnan==True :   
       qmD=0
        
    #朗缪尔系数
    G.append('Equilibrium Constant of Langmuir [m^3/mol]')
    print('Equilibrium Constant of Langmuir [m^3/mol]')

    bA=table.iloc[k,6]
    bAnan=np.isnan(bA)   
    if bAnan == False and yA != 0: 
       print('A : ', bA)   
       bA_output='A : '+str(bA)
       G.append(bA_output)
    if bAnan==True and yA != 0:
       print('A : ') 
       bA_output='A : '
       G.append(bA_output)
    if bAnan==True :   
       bA=0
     
    bB=table.iloc[k,7]
    bBnan=np.isnan(bB)
    if bBnan == False and yB != 0:
       print('B : ', bB) 
       bB_output='B : '+str(bB)
       G.append(bB_output)
    if bBnan==True and yB != 0:
       print('B : ') 
       bB_output='B : '
       G.append(bB_output)
    if bBnan==True :   
       bB=0
       
    bC=table.iloc[k,8]
    bCnan=np.isnan(bC)
    if bCnan == False and yC != 0:
       print('C : ', bC) 
       bC_output='C : '+str(bC)
       G.append(bC_output)
    if bCnan==True and yC != 0:
       print('C : ') 
       bC_output='C : '
       G.append(bC_output)
    if bCnan==True :   
       bC=0
       
    bD=table.iloc[k,9]
    bDnan=np.isnan(bD)
    if bDnan == False and yD != 0:
       print('D : ', bD) 
       bD_output='D : '+str(bD)
       G.append(bD_output)
    if bDnan==True and yD != 0:
       print('D : ')  
       bD_output='D : '
       G.append(bD_output)
    if bDnan==True :   
       bD=0

    #传质系数
    G.append('Overall Mass Transfer Coefficient [s^-1]')
    print('Overall Mass Transfer Coefficient [s^-1]')

    if bA == 0 :
       KAs=0
    if bA != 0 :
       KAs=table.iloc[k,10]
    KAsnan=np.isnan(KAs)
    if KAsnan==False and yA != 0:  
       print('A : ', KAs)  
       KAs_output='A : '+str(KAs)
       G.append(KAs_output)
    if KAsnan==True and yA != 0:
       print('A : ') 
       KAsnan_output='A : '
       G.append(KAsnan_output)
    if KAsnan==True :   
       KAs=0
           
    if bB == 0 :
       KBs=0
    if bB != 0 :
       KBs=table.iloc[k,11]
    KBsnan=np.isnan(KBs)
    if KBsnan==False and yB != 0:
       print('B : ', KBs) 
       KBs_output='B : '+str(KBs)
       G.append(KBs_output)
    if KBsnan==True and yB != 0:
       print('B : ') 
       KBsnan_output='B : '
       G.append(KBsnan_output)
    if KBsnan==True :   
       KBs=0
           
    if bC == 0 :
       KCs=0
    if bC != 0 :
       KCs=table.iloc[k,12]
    KCsnan=np.isnan(KCs)
    if KCsnan==False and yC != 0:
       print('C : ', KCs) 
       KCs_output='C : '+str(KCs)
       G.append(KCs_output)
    if KCsnan==True and yC != 0:
       print('C : ') 
       KCsnan_output='C : '
       G.append(KCsnan_output)
    if KCsnan==True :   
       KCs=0
           
    if bD == 0 :
       KDs=0
    if bD != 0 :
       KDs=table.iloc[k,13]
    KDsnan=np.isnan(KDs)
    if KDsnan==False and yD != 0:
       print('D : ', KDs) 
       KDs_output='D : '+str(KDs)
       G.append(KDs_output)
    if KDsnan==True and yD != 0:
       print('D : ') 
       KDsnan_output='D : '
       G.append(KDsnan_output)
    if KDsnan==True :   
       KDs=0

    G.append('')
    G.append('Simulation Finish')
    G.append('----------------------------------------------------------------------')
    G.append('')


    #检查EXCEL
    filename_input_Warning3 = "Excel_Error.txt" 
    if yA != 0:
       if qmAnan==True or bAnan==True or KAsnan==True :
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
          
    if yB != 0:
       if qmBnan==True or bBnan==True or KBsnan==True :
          print('Warning:Invalid parameters in excel table, please check.')
          Material_output='Material : ' + str(No_or_Name)
          if Material_output not in G:   
             G.append(Material_output)#OUTPUT编   
          G.append('')
          G.append('Warning:Invalid parameters for component B in excel table, please check.')      
          output_input_Warning3=open(r'OUTPUT/%s'%(filename_input_Warning3),'w')
          for l in range(len(G)):
              output_input_Warning3.write(str(G[l]))
              #output_input_Warning3.write("\t")#空4个字符 可以不加
              output_input_Warning3.write("\n")#\n换行
          output_input_Warning3.close()
          sys.exit() #终止程序

    if yC != 0:
       if qmCnan==True or bCnan==True or KCsnan==True :
          print('Warning:Invalid parameters in excel table, please check.')
          Material_output='Material : ' + str(No_or_Name)
          if Material_output not in G:   
             G.append(Material_output)#OUTPUT编   
          G.append('')
          G.append('Warning:Invalid parameters for component C in excel table, please check.')      
          output_input_Warning3=open(r'OUTPUT/%s'%(filename_input_Warning3),'w')
          for l in range(len(G)):
              output_input_Warning3.write(str(G[l]))
              #output_input_Warning3.write("\t")#空4个字符 可以不加
              output_input_Warning3.write("\n")#\n换行
          output_input_Warning3.close()
          sys.exit() #终止程序     

    if yD != 0:
       if qmDnan==True or bDnan==True or KDsnan==True :
          print('Warning:Invalid parameters in excel table, please check.')
          Material_output='Material : ' + str(No_or_Name)
          if Material_output not in G:   
             G.append(Material_output)#OUTPUT编   
          G.append('')
          G.append('Warning:Invalid parameters for component D in excel table, please check.')      
          output_input_Warning3=open(r'OUTPUT/%s'%(filename_input_Warning3),'w')
          for l in range(len(G)):
              output_input_Warning3.write(str(G[l]))
              #output_input_Warning3.write("\t")#空4个字符 可以不加
              output_input_Warning3.write("\n")#\n换行
          output_input_Warning3.close()
          sys.exit() #终止程序

    #开始准备计算
    #换时间单位为h
    KA=KAs*3600
    KB=KBs*3600
    KC=KCs*3600
    KD=KDs*3600
          
    for iteration in np.arange(1,max_iteration+1) :  
        
        T=int(iteration*T_first)
        print('')
        print('Iteration : ',iteration)
        #建立网格
        A=np.zeros([Z+1,T+1])
        B=np.zeros([Z+1,T+1])
        C=np.zeros([Z+1,T+1])
        D=np.zeros([Z+1,T+1])

        qA=np.zeros([Z+1,T+1])
        qB=np.zeros([Z+1,T+1])
        qC=np.zeros([Z+1,T+1])
        qD=np.zeros([Z+1,T+1])
            
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

        #边界条件
        for j in np.arange(1,T+1):
            A[0,j]=CA_0
            B[0,j]=CB_0
            C[0,j]=CC_0
            D[0,j]=CD_0
            qA[Z,j]=0
            qB[Z,j]=0
            qC[Z,j]=0
            qD[Z,j]=0
           
        #初始条件
        for i in np.arange(0,Z+1):
            A[i,0]=0
            B[i,0]=0
            C[i,0]=0
            D[i,0]=0
            qA[i,0]=0
            qB[i,0]=0
            qC[i,0]=0
            qD[i,0]=0
            
                
        #递推关系
        for j in np.arange(0,T):
            for i in np.arange(1,Z):
          #吸附量
        #A     
                if yA != 0:             
                   A[i,j+1]=dt*(((DLA/(dz**2))+v/dz)*A[i-1,j]+(1/dt-v/dz-(2*DLA)/(dz**2))*A[i,j]+(DLA/(dz**2))*A[i+1,j]
                                    -(Ps*((1-eb)/eb)*KA*(((bA*qmA*A[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qA[i,j])))
                   
                   qA[i,j+1]=KA*dt*(((bA*qmA*A[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qA[i,j])+qA[i,j]
                   
                
              
        #B      
                if yB != 0:      
                   B[i,j+1]=dt*(((DLB/(dz**2))+v/dz)*B[i-1,j]+(1/dt-v/dz-(2*DLB)/(dz**2))*B[i,j]+(DLB/(dz**2))*B[i+1,j]
                                    -(Ps*((1-eb)/eb)*KB*(((bB*qmB*B[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qB[i,j])))
                   
                   qB[i,j+1]=KB*dt*(((bB*qmB*B[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qB[i,j])+qB[i,j]
                   
                
                   
        #C     
                if yC != 0:           
                   C[i,j+1]=dt*(((DLC/(dz**2))+v/dz)*C[i-1,j]+(1/dt-v/dz-(2*DLC)/(dz**2))*C[i,j]+(DLC/(dz**2))*C[i+1,j]
                                    -(Ps*((1-eb)/eb)*KC*(((bC*qmC*C[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qC[i,j])))
                   
                   qC[i,j+1]=KC*dt*(((bC*qmC*C[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qC[i,j])+qC[i,j]
                   
                
                   
        #D     
                if yD != 0:                       
                   D[i,j+1]=dt*(((DLD/(dz**2))+v/dz)*D[i-1,j]+(1/dt-v/dz-(2*DLD)/(dz**2))*D[i,j]+(DLD/(dz**2))*D[i+1,j]
                                    -(Ps*((1-eb)/eb)*KD*(((bD*qmD*D[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qD[i,j])))
                   
                   qD[i,j+1]=KD*dt*(((bD*qmD*D[i,j])/(1+bA*A[i,j]+bB*B[i,j]+bC*C[i,j]+bD*D[i,j]))-qD[i,j])+qD[i,j]
                   
        #自测不收敛提前中止  
                nanA=np.isnan(A[i,j+1])
                nanB=np.isnan(B[i,j+1])
                nanC=np.isnan(C[i,j+1])
                nanD=np.isnan(D[i,j+1])
                if A[i,j+1] > cmax or B[i,j+1] > cmax or C[i,j+1] > cmax or D[i,j+1] > cmax or nanA ==True or nanB ==True or nanC ==True or nanD ==True or qA[i,j+1] < 0 or qB[i,j+1] < 0 or qC[i,j+1] < 0 or qD[i,j+1] < 0:
                   break 
                                
            for i in np.arange(Z,Z+1):
                if yA != 0:
                   A[i,j+1]=A[i-1,j+1]
                   
                if yB != 0:
                   B[i,j+1]=B[i-1,j+1]
                   
                if yC != 0:
                   C[i,j+1]=C[i-1,j+1]
                   
                if yD != 0:   
                    D[i,j+1]=D[i-1,j+1]

        #自测不收敛提前中止
                nanA=np.isnan(A[i,j+1])
                nanB=np.isnan(B[i,j+1])
                nanC=np.isnan(C[i,j+1])
                nanD=np.isnan(D[i,j+1])
                if A[i,j+1] > cmax or B[i,j+1] > cmax or C[i,j+1] > cmax or D[i,j+1] > cmax or nanA ==True or nanB ==True or nanC ==True or nanD ==True :
                   break         
        
        print('Finish')
        print('--------------------------------------------------')

        #检查       
        A_min=np.min(A)
        A_max=np.max(A)
        qA_min=np.min(qA)
        nanA_max=np.isnan(A_max)#nan判定
        nanA_min=np.isnan(A_min)
        nanqA_min=np.isnan(qA_min)
            
        B_min=np.min(B)
        B_max=np.max(B)
        qB_min=np.min(qB)
        nanB_max=np.isnan(B_max)
        nanB_min=np.isnan(B_min)
        nanqB_min=np.isnan(qB_min)
            
        C_min=np.min(C)
        C_max=np.max(C)
        qC_min=np.min(qC)
        nanC_max=np.isnan(C_max)
        nanC_min=np.isnan(C_min)
        nanqC_min=np.isnan(qC_min)
            
        D_min=np.min(D)
        D_max=np.max(D)
        qD_min=np.min(qD)
        nanD_max=np.isnan(D_max)
        nanD_min=np.isnan(D_min)
        nanqD_min=np.isnan(qD_min)

        print('Begin to identify breakthrough times')

        #是否计算穿透时间  
        
           
        if BTTC=='Yes' :   
           if A_min<0  or qA_min<0 or A_max>cmax or B_min<0 or qB_min<0 or B_max>cmax or C_min<0  or qC_min<0 or C_max>cmax or  D_min<0  or qD_min<0 or D_max>cmax or nanA_max==True or nanA_min==True or nanqA_min==True or nanB_max==True or nanB_min==True or nanqB_min==True or nanC_max==True or nanC_min==True or nanqC_min==True or nanD_max==True or nanD_min==True or nanqD_min==True:
              print('Warning : It was not converge. Please try to set smaller Time Step Length & Space Step Length.')
                                
           if A_min==0 and  qA_min==0 and A_max<=cmax and B_min==0 and  qB_min==0 and B_max<=cmax and C_min==0 and  qC_min==0 and C_max<=cmax and D_min==0 and qD_min==0 and D_max<=cmax :
#计算突破时间
              if yA !=0 :
                 for tA in np.arange(0,T+1):
                     C_A = A[Z,tA]
                     dC_A = C_A - CA_10
                     if dC_A >= 0 :
                        t_A = tA
                        #print(t_A)
                        break #中止运行循环 continue表示跳过条件，继续运行
                     if tA==T and dC_A<0 :                 
                        print('Warning : please set larger Time Steps for A')
                     
              if yA ==0 :
                 t_A=0
                 dC_A=0
               
               
              if yB !=0 :
                 for tB in np.arange(0,T+1):
                     C_B = B[Z,tB]
                     dC_B = C_B - CB_10
                     if dC_B >= 0 :
                        t_B = tB
                        #print(t_B)
                        break #中止运行循环 continue表示跳过条件，继续运行
                     if tB==T and dC_B<0 :
                        print('Warning : please set larger Time Steps for B')
                     
              if yB ==0 :
                 t_B=0 
                 dC_B=0

                      
              if yC !=0 :
                 for tC in np.arange(0,T+1):
                     C_C = C[Z,tC]
                     dC_C = C_C - CC_10
                     if dC_C >= 0 :
                        t_C = tC
                        #print(t_C)
                        break #中止运行循环 continue表示跳过条件，继续运行
                     if tC==T and dC_C<0 :
                        print('Warning : please set larger Time Steps for C')
                     
              if yC ==0 :
                 t_C=0
                 dC_C=0

                      
              if yD !=0 :
                 for tD in np.arange(0,T+1):
                     C_D = D[Z,tD]
                     dC_D = C_D - CD_10
                     if dC_D >= 0 :
                        t_D = tD
                        #print(t_D)
                        break #中止运行循环 continue表示跳过条件，继续运行
                     if tD==T and dC_D<0 :
                        print('Warning : please set larger Time Steps for D')
                     
              if yD ==0 :
                 t_D=0 
                 dC_D=0      
                             
              
              if dC_A<0 or dC_B<0 or dC_C<0 or dC_D<0 :              
                 del A 
                 del B 
                 del C 
                 del D 
                 del qA 
                 del qB 
                 del qC
                 del qD
                 del space_time
                 gc.collect()
                 gc.DEBUG_UNCOLLECTABLE
                 del gc.garbage[:]
                 
                 if iteration == max_iteration :
                    print('Warning : the setting of max_iteration and minimum Time step may be not long enough.Please check.')                      
                    print('Finish')
                                     
                    
              if dC_A>=0 and dC_B>=0 and dC_C>=0 and dC_D>=0 :
                 print('Breakthrough time : ')                 
                 if yA !=0 :
                    x_A=space_time[0:t_A]
                    y_A=A[Z,0:t_A]
                    KNEE_A=KneeLocator(x_A,y_A,curve='convex',direction='increasing',online=False)
                    print('A   [h] : ',KNEE_A.elbow)
                    print('  [min] : ',KNEE_A.elbow*60)
                    print('    [s] : ',KNEE_A.elbow*3600)
                    print('C/C0 for Breakthrough Time : ',KNEE_A.elbow_y/CA_0)
                    
                 if yB !=0 : 
                    x_B=space_time[0:t_B] 
                    y_B=B[Z,0:t_B] 
                    KNEE_B=KneeLocator(x_B,y_B,curve='convex',direction='increasing',online=False)
                    print('B   [h] : ',KNEE_B.elbow)
                    print('  [min] : ',KNEE_B.elbow*60)
                    print('    [s] : ',KNEE_B.elbow*3600)
                    print('C/C0 for Breakthrough Time : ',KNEE_B.elbow_y/CB_0)
                    
                 if yC !=0 :  
                    x_C=space_time[0:t_C] 
                    y_C=C[Z,0:t_C] 
                    KNEE_C=KneeLocator(x_C,y_C,curve='convex',direction='increasing',online=False)
                    print('C   [h] : ',KNEE_C.elbow)      
                    print('  [min] : ',KNEE_C.elbow*60)
                    print('    [s] : ',KNEE_C.elbow*3600)
                    print('C/C0 for Breakthrough Time : ',KNEE_C.elbow_y/CC_0)
                    
                 if yD !=0 :  
                    x_D=space_time[0:t_D] 
                    y_D=D[Z,0:t_D] 
                    KNEE_D=KneeLocator(x_D,y_D,curve='convex',direction='increasing',online=False)
                    print('D   [h] : ',KNEE_D.elbow)
                    print('  [min] : ',KNEE_D.elbow*60)
                    print('    [s] : ',KNEE_D.elbow*3600)
                    print('C/C0 for Breakthrough Time : ',KNEE_D.elbow_y/CD_0)
                 
                 print('Finish')
                 print('--------------------------------------------------')
                 
                 break                                        
    def Breakthrough_times_output():
        print("Begin to ouput breakthrough times")
        
        if BTTC=='No' :
           print('Warning:This is the setting for breakthrough curves calculation without the calculation of breakthrough times.')
           Material_output='Material : ' + str(No_or_Name)
           if Material_output not in G:   
              G.append(Material_output)#OUTPUT编号
              
           G.append('')
           
           if "Warning:This is the setting for breakthrough curves calculation without the calculation of breakthrough times." not in G:
              G.append('Warning:This is the setting for breakthrough curves calculation without the calculation of breakthrough times.')        
           
           if A_min<0  or qA_min<0 or A_max>cmax or B_min<0 or qB_min<0 or B_max>cmax or C_min<0  or qC_min<0 or C_max>cmax or  D_min<0  or qD_min<0 or D_max>cmax or nanA_max==True or nanA_min==True or nanqA_min==True or nanB_max==True or nanB_min==True or nanqB_min==True or nanC_max==True or nanC_min==True or nanqC_min==True or nanD_max==True or nanD_min==True or nanqD_min==True:
              print('Warning : It was not converge. Please try to set smaller Time Step Length or Space Step Length.')
              if "Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length." not in G:
                 G.append('Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length.')
                 
           filename_time_error1 = "OUTPUT_" + str(No_or_Name) + ".txt"
           output_time_error1=open(r'OUTPUT/%s'%(filename_time_error1),'w')#带有变量，字符中带有变量，‘%s'%(变量)
           for l in range(len(G)):
               output_time_error1.write(str(G[l]))
               #output_time_error1.write("\t")
               output_time_error1.write("\n")
           output_time_error1.close()

           print('Finish')
           print('--------------------------------------------------')
        
        if BTTC=='Yes' :        
           
           if A_min<0  or qA_min<0 or A_max>cmax or B_min<0 or qB_min<0 or B_max>cmax or C_min<0  or qC_min<0 or C_max>cmax or  D_min<0  or qD_min<0 or D_max>cmax or nanA_max==True or nanA_min==True or nanqA_min==True or nanB_max==True or nanB_min==True or nanqB_min==True or nanC_max==True or nanC_min==True or nanqC_min==True or nanD_max==True or nanD_min==True or nanqD_min==True:
              print('Warning : It was not converge. Please try to set smaller Time Step Length or Space Step Length.')
              Material_output='Material : ' + str(No_or_Name)
              if Material_output not in G:   
                 G.append(Material_output)#OUTPUT编号

              G.append('')
              
              if "Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length." not in G:
                 G.append('Warning : It can not converge. Please try to set smaller Time Step Length or Space Step Length.')        
                 
              filename_time_error2 = "OUTPUT_" + str(No_or_Name) + ".txt"
              output_time_error2=open(r'OUTPUT/%s'%(filename_time_error2),'w')#带有变量，字符中带有变量，‘%s'%(变量)
              for l in range(len(G)):
                  output_time_error2.write(str(G[l]))
                  #output_time_error2.write("\t")
                  output_time_error2.write("\n")
              output_time_error2.close()

              print('Finish')
              print('--------------------------------------------------')
                                 
           if A_min==0 and  qA_min==0 and A_max<=cmax and B_min==0 and  qB_min==0 and B_max<=cmax and C_min==0 and  qC_min==0 and C_max<=cmax and D_min==0 and qD_min==0 and D_max<=cmax :
              
              if dC_A<0 or dC_B<0 or dC_C<0 or dC_D<0 :                                               
                 if iteration == max_iteration :
                    print('Warning : the setting of max_iteration and minimum Time step may be not long enough.Please check.')
                    Material_output='Material : ' + str(No_or_Name)
                    if Material_output not in G:   
                       G.append(Material_output)#OUTPUT编号
                       
                    G.append('')
                    
                    if 'Warning : the setting of max_iteration and minimum Time step may be not long enough.Please check.' not in G:         
                       G.append('Warning : the setting of max_iteration and minimum Time step may be not long enough.Please check.')
                    
                    filename_time_output1 = "OUTPUT_" + str(No_or_Name) + ".txt"
                    output_time_output=open(r'OUTPUT/%s'%(filename_time_output1),'w')#带有变量，字符中带有变量，‘%s'%(变量)
                    for l in range(len(G)):
                        output_time_output.write(str(G[l]))
                        #output_time_output.write("\t")
                        output_time_output.write("\n")
                    output_time_output.close()  

                    print('Finish')
                  
              if dC_A>=0 and dC_B>=0 and dC_C>=0 and dC_D>=0 :          
    #导出结果
                 Material_output='Material : ' + str(No_or_Name)
                 if Material_output not in G:   
                    G.append(Material_output)#OUTPUT编号
    #OUTPUT编号
                 G.append('')
    #导出突破时间             
                 if yA !=0 :
                    Component_A_OUTPUT='Component A : ' + A_name
                    T_A_output_h = 'Breakthrough Time [h] : ' + str(KNEE_A.elbow)
                    T_A_output_min = '                [min] : ' + str(KNEE_A.elbow*60)
                    T_A_output_s = '                  [s] : ' + str(KNEE_A.elbow*3600)
                    C_A_C_A0_output = 'C/C0 for Breakthrough Time : ' + str(KNEE_A.elbow_y/CA_0) 
                       
                    if T_A_output_h and T_A_output_min and T_A_output_s not in G :
                       G.append(Component_A_OUTPUT) 
                       G.append(T_A_output_h)
                       G.append(T_A_output_min)
                       G.append(T_A_output_s)
                    if C_A_C_A0_output not in G:
                       G.append('')  
                       G.append(C_A_C_A0_output)
                       G.append('')  
                   
                 if yB !=0 :
                    Component_B_OUTPUT='Component B : ' + B_name
                    T_B_output_h = 'Breakthrough Time [h] : ' + str(KNEE_B.elbow)
                    T_B_output_min = '                [min] : ' + str(KNEE_B.elbow*60)
                    T_B_output_s = '                  [s] : ' + str(KNEE_B.elbow*3600)
                    C_B_C_B0_output = 'C/C0 for Breakthrough Time : ' + str(KNEE_B.elbow_y/CB_0)

                    if T_B_output_h and T_B_output_min and T_B_output_s not in G :
                       G.append(Component_B_OUTPUT) 
                       G.append(T_B_output_h)
                       G.append(T_B_output_min)
                       G.append(T_B_output_s)
                    if C_B_C_B0_output not in G:
                       G.append('') 
                       G.append(C_B_C_B0_output)
                       G.append('')
                       
                 if yC !=0 :
                    Component_C_OUTPUT='Component C : ' + C_name
                    T_C_output_h = 'Breakthrough Time [h] : ' + str(KNEE_C.elbow)
                    T_C_output_min = '                [min] : ' + str(KNEE_C.elbow*60)
                    T_C_output_s = '                  [s] : ' + str(KNEE_C.elbow*3600)
                    C_C_C_C0_output = 'C/C0 for Breakthrough Time : ' + str(KNEE_C.elbow_y/CC_0)

                    if T_C_output_h and T_C_output_min and T_C_output_s not in G :
                       G.append(Component_C_OUTPUT) 
                       G.append(T_C_output_h)
                       G.append(T_C_output_min)
                       G.append(T_C_output_s)
                    if C_C_C_C0_output not in G:
                       G.append('') 
                       G.append(C_C_C_C0_output)
                       G.append('') 
                       
                 if yD !=0 :
                    Component_D_OUTPUT='Component D : ' + D_name
                    T_D_output_h = 'Breakthrough Time [h] : ' + str(KNEE_D.elbow)
                    T_D_output_min = '                [min] : ' + str(KNEE_D.elbow*60)
                    T_D_output_s = '                  [s] : ' + str(KNEE_D.elbow*3600)
                    C_D_C_D0_output = 'C/C0 for Breakthrough Time : ' + str(KNEE_D.elbow_y/CD_0)

                    if T_D_output_h and T_D_output_min and T_D_output_s not in G :
                       G.append(Component_D_OUTPUT) 
                       G.append(T_D_output_h)
                       G.append(T_D_output_min)
                       G.append(T_D_output_s)
                    if C_D_C_D0_output not in G:
                       G.append('') 
                       G.append(C_D_C_D0_output)      
                       G.append('')
                       
                 filename_time_output = "OUTPUT_" + str(No_or_Name) + ".txt"
                 output_time_output=open(r'OUTPUT/%s'%(filename_time_output),'w')#带有变量，字符中带有变量，‘%s'%(变量)
                 for l in range(len(G)):
                     output_time_output.write(str(G[l]))
                     #output_time_output.write("\t")
                     output_time_output.write("\n")
                 output_time_output.close()

           print('Finish')
           
        return print('--------------------------------------------------')
    
    if type=='Breakthrough_times_output'  :
       return Breakthrough_times_output()
            
                    
if __name__ == "__main__" :
   BTTC() #import时不会被启用
    
    

 
          

         
             

      
