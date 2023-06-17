import pandas as pd
import numpy as np
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    data_transformed=data.copy()

# In[3]:


    data_transformed['price']=data['price'].str.replace(',','').str.replace('.', '').fillna('-20').astype(int).replace({-20:np.nan})

    # In[4]:


    def transform_rating(df):
        try :

            df=df.split()[0]
            return df

        except AttributeError:
            return df


    # In[5]:


    
    data_transformed['rating']=data_transformed['rating'].apply(lambda x: transform_rating(x))
    data_transformed['rating'][data_transformed['rating'].apply(lambda x: len(x) > 3)]=np.nan


    # In[6]:


    data_transformed['rating']=data_transformed['rating'].astype(float)
   


    # In[7]:


    def convert_units(value):
        
        parts = value.split()
        converted_value=0
            
        if len(parts) == 2:
            numeric_part = float(parts[0])
            unit = parts[1]
                
            if unit == 'cm':
                converted_value = numeric_part * 0.393701  # Convert cm to inches
            else:
                converted_value = numeric_part  # Keep the original value
            
            
        
        return converted_value

    # In[8]:


    strings =data_transformed['screen_size'].apply(lambda x: transform_rating(x))
    index=strings[strings.apply(lambda x: len(x) > 4)].index


    # In[9]:


    
    # In[10]:


    data_transformed['screen_size']=data_transformed['screen_size'].apply(lambda x: convert_units(x))

    # In[11]:


    
    # In[12]:


    
    # In[13]:


    import re
    def convert_abnormal_value(value):
        
        match = re.search(r'\d+(\.\d+)?', value)
        if match:
            return float(match.group())
        if re.match(r'^\d+(\.\d+)?$', value):
            return float(value)
        else:
            return float('nan')


    # In[14]:


    
    # In[15]:


   


    data_transformed['battery_power']=data_transformed['battery_power'].apply(convert_abnormal_value)


    # In[17]:


    def transform_ram(df):
        try :

            df=int(df.split()[0])
            return df

        except ValueError:
            return np.nan

    # In[18]:


    data_transformed['ram'].apply(lambda x: transform_ram(x)).value_counts()


    # In[21]:


    data_transformed['ram']=data_transformed['ram'].apply(lambda x: transform_ram(x))

    # Here  some ram values are abnormal  with storage space having less than them , lets eliminate those values

    # In[22]:


    

    # In[23]:


    data_transformed['ram'][data_transformed['ram']>16] = np.nan

    # In[24]:


    
    # In[81]:


    def transform_storage(df):
        try :
            if len(df.split())>1 and df.split()[1] != 'MB':
                df=int(df.split()[0])
                return df

            
            return np.nan

        except ValueError:
            return np.nan

    # In[71]:


    

    # In[88]:


    data_transformed['storage']=data_transformed['storage'].apply(lambda x: transform_storage(x))

    # In[91]:



    # data_transformed[data_transformed['storage'].apply(lambda x: transform_storage(x))==512]
    data_transformed['storage'][data_transformed['storage']<12]=np.nan

    # In[94]:


    def transform_weight(df):
        try :
            
            df=int(df.split()[0])
            return df


        except ValueError:
            return np.nan

    # In[98]:


    

    # In[99]:


    

    # In[102]:


    data_transformed['item_weight']=data_transformed['item_weight'].apply(lambda x: transform_weight(x))

    # In[104]:


    

    # In[105]:


    # Remove the column 'Unnamed: 0'
    data_transformed = data_transformed.drop('Unnamed: 0', axis=1)

    # Rename the columns
    data_transformed = data_transformed.rename(columns={
        'screen_size': 'screen_size_inches',
        'ram': 'ram_GB',
        'storage': 'storage_GB',
        'item_weight': 'item_weight_grams'
    })








    # In[108]:


    data_transformed = data_transformed.rename(columns={
        'battery_power': 'battery_power_MAH'})
    data_transformed['brand']=data_transformed['brand'].str.upper()
    data_transformed[data_transformed['brand']=='POCO BY XIAOMI']['brand']='POCO'

    
    return data_transformed


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
