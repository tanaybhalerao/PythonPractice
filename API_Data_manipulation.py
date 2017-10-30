from marketorestpython.client import MarketoClient
import pandas as pd
from datetime import date as dt,timedelta
import psycopg2 as pg
from sqlalchemy import create_engine

class Activity:

    def __init__(self):
        self.munchkin_id = 
        self.client_id = 
        self.client_secret = 
        self.mc = MarketoClient(self.munchkin_id, self.client_id, self.client_secret)

    def activity_list(self):
        act_list = self.mc.execute(method='get_activity_types')
        act_list_df = pd.DataFrame(act_list)
        alist = act_list_df['id'].tolist()
        return alist

    def lead_activities(self, activities, start_dt):
        activity_list = self.mc.execute(method='get_lead_activities', activityTypeIds=activities,nextPageToken=None, sinceDatetime=start_dt)
        act_df = pd.DataFrame(activity_list)
        acti_df1 = pd.concat([pd.DataFrame(x) for x in act_df['attributes']], keys=act_df.index).reset_index(level=1, drop=True)
        adf = act_df.drop('attributes', axis=1).join(acti_df1).reset_index(drop=True)
        return adf

    def yld_lead_acti(self,activities,start_dt):
        for activities in self.mc.execute(method='get_lead_activities_yield',activityTypeIds=activities,nextPageToken=None, sinceDatetime=start_dt):
            print(len(activities))
            act_df=pd.DataFrame(activities)
            acti_df1= pd.concat([pd.DataFrame(x) for x in act_df['attributes']], keys=act_df.index).reset_index(level=1, drop=True)
            adf = act_df.drop('attributes', axis=1).join(acti_df1).reset_index(drop=True)
            return adf
  
    def truncate_db(self,df):
        con = pg.connect(database="dw_prod", user="mscorpsys", password="PHwuI2yDJ9bC",host="gp_dw_prod.dw.neustar.biz", port="5435")
        cur=con.cursor()
        # cur.execute('Truncate stage_activity;')
        df.to_sql()
        # colnames = [desc[0] for desc in cur.description]
        # print(colnames)
        print("done")

    def load_df(self,df):
        engine = create_engine('postgresql://mscorpsys:PHwuI2yDJ9bC@gp_dw_prod.dw.neustar.biz:5435/dw_prod')
        # print(pd.read_sql_table('stage_activity',engine))

        df.to_sql('stage_activity',engine,if_exists='append',schema='marketo',index=False)
        print("success")



Ack=Activity()
alist=Ack.activity_list()

for activity in alist:
    activity_df=Ack.yld_lead_acti(str(activity),dt.today()-timedelta(1))
    Ack.load_df(activity_df)
    break

# Ack.truncate_db()

# Ack.load_df()