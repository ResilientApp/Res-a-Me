<template>
    <v-expansion-panel >
      <v-expansion-panel-title >
        <template v-slot:default="{expanded}">
          <v-row no-gutters class="d-flex jusitfy-start">
            <h1 style="font-weight: 500;">Professional Experience</h1>
            <v-icon class="ml-2"
                        size="xx-large"
                        icon="mdi-briefcase-outline"
            ></v-icon>
          </v-row>
        </template>
      </v-expansion-panel-title>
          <v-expansion-panel-text>
            <template v-for="(pro, index) in professions" :key="index">
              <div class="mb-3" style="border:2px solid rgb(198, 194, 194)">
                <v-row no-gutters>
                    <v-col cols="11" >
                      <v-row no-gutters>
                        <v-col cols="3">
                          <v-text-field
                            class="pa-2"
                            v-model="pro.company"
                            :rules="[
                                () => isCompanyValid(pro) || 'This field is required'
                            ]"
                            :counter="20"
                            label="Company"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="4">
                          <v-text-field
                            class="pa-2"
                            v-model="pro.title"
                            :rules="[
                                () => isPositionValid(pro) || 'This field is required'
                            ]"
                            :counter="30"
                            label="Position"
                          ></v-text-field>
                        </v-col>
                        <v-col >
                          <v-text-field
                            class="pa-2"
                            v-model="pro.startDate"
                            :rules="[
                                () => !!pro.startDate || 'This field is required',
                                () => isStartDateValid(pro) || 'Date must be in YYYY/MM format'
                            ]"
                            :counter="10"
                            label="Start Date"
                          ></v-text-field>
                        </v-col>
                        <v-col >
                          <v-text-field
                            class="pa-2"
                            v-model="pro.endDate"
                            :rules="[
                                () => !!pro.endDate || 'This field is required',
                                () => isEndDateValid(pro) || 'Date must be in YYYY/MM format'
                            ]"
                            :counter="10"
                            label="End Date"
                          ></v-text-field>
                        </v-col>
                      </v-row>
                      <v-row no-gutters>
                        <v-text-field
                            class="pl-2 pr-2"
                            v-model="pro.description"
                            :rules="[
                                () => isDescriptionValid(pro)|| 'This field is required'
                            ]"
                            :counter="300"
                            label="Description"
                        ></v-text-field>
                      </v-row>
                    </v-col>
                    <v-col class="button-container">
                      <v-btn @click="deletePro(index)" color="red-lighten-2"
                      >
                        <v-icon
                          size="x-large"
                          icon="mdi-trash-can"
                        ></v-icon>
                      </v-btn>
                    </v-col>
                </v-row>
              </div>
            </template>
            <div class="d-flex justify-center">
              <v-btn color="grey-lighten-1" @click="addNewPro()"
                      >Add more
                        <v-icon
                          size="x-large"
                          icon="mdi-plus-thick"
                        ></v-icon>
              </v-btn>
              <v-btn class="ml-5" color="green" @click="savePro(professions)"
                      >Save
                        <v-icon 
                          size="x-large"
                          icon="mdi-content-save"
                        ></v-icon>
              </v-btn>
            </div>
          </v-expansion-panel-text>
    </v-expansion-panel>
  </template>
  
  
  <script>
    import { ref, watch, onMounted, toRef } from 'vue';
    export default {
      props: ['professions'],
      
      setup(props,{emit}) {

          // watch(() => props.professions, (newPros, oldPros) => {
          //   console.log('New value:', newPros);
          //   console.log('Old value:', oldPros);
          // });
          const isCompanyValid = (pro) => {
              return !!pro.company;
          };
          const isPositionValid = (pro) => {
              return !!pro.title;
          };
          const isStartDateValid = (pro) => {
              return !!pro.startDate && /\b\d{4}\/(0[1-9]|1[0-2])\b/.test(pro.startDate);
          };
          const isEndDateValid = (pro) => {
              return !!pro.endDate && /\b\d{4}\/(0[1-9]|1[0-2])\b/.test(pro.endDate);;
          };
          const isDescriptionValid = (pro) => {
              return !!pro.description;
          };

          const deletePro = (index) => {
            if(index != -1){
              emit('delete-pro',index);
            }
          };
          const addNewPro = ()=>{
            emit('add-pro');
  
          };
          const savePro=(professions)=>{
            let allRulesPassed = true;            
              professions.forEach((pro, index) => {
                if (!isCompanyValid(pro) ||
                    !isPositionValid(pro) ||
                    !isStartDateValid(pro) ||
                    !isEndDateValid(pro) ||
                    !isDescriptionValid(pro)) {
                    allRulesPassed = false;
                }
              });
            if (allRulesPassed) {
                // console.log('data format is correct')
                alert('Your Profession information has been saved!')
                emit('save-pro', professions);
            } else {
                confirm('Some fields may be incorrect. Please check!')
            }
          }
  
          return {
            deletePro,
            addNewPro,
            savePro,
            isCompanyValid,
            isPositionValid,
            isDescriptionValid,
            isStartDateValid,
            isEndDateValid
          };
      },
  
      
    };
  </script>
  
  
  <style>
  .button-container {
    display: flex;
    flex-direction: row; /* Vertical layout */
    align-items: center; /* Center items horizontally */
    justify-content: center; /* Center items vertically */
  }
  </style>