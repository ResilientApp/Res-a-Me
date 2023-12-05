<template>
    <v-expansion-panel >
      <v-expansion-panel-title id="title">
        <template v-slot:default="{expanded}">
          <v-row no-gutters class="d-flex jusitfy-start">
            <p class="titletext">Award</p>
            <v-icon class="ml-2"
                        size="xx-large"
                        icon="mdi-license"
            ></v-icon>
          </v-row>
        </template>
      </v-expansion-panel-title>
          <v-expansion-panel-text>
            <template v-for="(award, index) in awards" :key="index">
              <div class="mb-3" style="border:2px solid rgb(198, 194, 194)">
                <v-row no-gutters>
                    <v-col cols="11" >
                      <v-row no-gutters>
                        <v-col cols="4">
                          <v-text-field
                            class="pa-2"
                            v-model="award.title"
                            :rules="[
                                () => isTitleValid(award) || 'This field is required'
                            ]"
                            :counter="40"
                            label="Title"
                          ></v-text-field>
                        </v-col>
                        <v-col cols="4">
                          <v-text-field
                            class="pa-2"
                            v-model="award.date"
                            :rules="[
                                () => !!award.date || 'This field is required',
                                () => isDateValid(award) || 'Date must be in YYYY/MM format'
                            ]"
                            :counter="20"
                            label="Date"
                          ></v-text-field>
                        </v-col>
                        <v-col >
                          <v-text-field
                            class="pa-2"
                            v-model="award.company_school"
                            :rules="[
                                () => isCompanySchoolValid(award) || 'This field is required'
                            ]"
                            :counter="10"
                            label="Company/School"
                          ></v-text-field>
                        </v-col>
                      </v-row>
                      <v-row no-gutters>
                        <v-text-field
                            class="pl-2 pr-2"
                            v-model="award.description"
                            :rules="[
                                () => isDescriptionValid(award)|| 'This field is required'
                            ]"
                            :counter="200"
                            label="Description"
                        ></v-text-field>
                      </v-row>
                    </v-col>
                    <v-col class="button-container">
                      <v-btn @click="deleteAward(index)" color="red-lighten-2"
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
              <v-btn color="grey-lighten-1" @click="addNewAward()"
                      >Add more
                        <v-icon
                          size="x-large"
                          icon="mdi-plus-thick"
                        ></v-icon>
              </v-btn>
              <v-btn class="ml-5" color="green" @click="saveAward(awards)"
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
      props: ['awards'],
      
      setup(props,{emit}) {

          // watch(() => props.awards, (newAwards, oldAwards) => {
          //   console.log('New value:', newAwards);
          //   console.log('Old value:', oldAwards);
          // });
          const isTitleValid = (award) => {
              return !!award.title;
          };
          const isCompanySchoolValid = (award) => {
              return !!award.company_school;
          };
          const isDateValid = (award) => {
              return !!award.date&& /\b\d{4}\/(0[1-9]|1[0-2])\b/.test(award.date);
          };
          const isDescriptionValid = (award) => {
              return !!award.description;
          };

          const deleteAward = (index) => {
            if(index != -1){
              emit('delete-award',index);
            }
          };
          const addNewAward = ()=>{
            emit('add-award');
  
          };
          const saveAward=(awards)=>{
            let allRulesPassed = true;            
            awards.forEach((award, index) => {
                if (!isTitleValid(award) ||
                    !isCompanySchoolValid(award) ||
                    !isDescriptionValid(award)) {
                    allRulesPassed = false;
                }
              });
            if (allRulesPassed) {
                // console.log('data format is correct')
                alert('Your Award information has been saved!')
                emit('save-award', awards);
            } else {
                confirm('Some fields may be incorrect. Please check!')
            }
          }
  
          return {
            deleteAward,
            addNewAward,
            saveAward,
            isTitleValid,
            isCompanySchoolValid,
            isDescriptionValid,
            isDateValid
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