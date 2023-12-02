<template>
    <v-expansion-panel>
        <v-expansion-panel-title>
            <template v-slot:default="{ expanded }">
                <v-row no-gutters class="d-flex jusitfy-start ">
                    <h1 style="font-weight: 500;">
                        About
                    </h1>
                    <v-icon class="ml-2" size="xx-large" icon="mdi-information-outline"></v-icon>
                </v-row>
            </template>
        </v-expansion-panel-title>
        <v-expansion-panel-text>
            <v-row no-gutters>
                <v-col>
                    <v-text-field class="pa-2" v-model="about.name" :rules="[
                        () => !!about.name || 'This field is required',
                        () => isNameValid() || 'Name must be at least 2 characters and less than 20 characters'
                    ]" :counter="20" label="Name"></v-text-field>
                </v-col>
                <v-col>
                    <v-text-field class="pa-2" v-model="about.role" :rules="[
                        () => !!about.role || 'This field is required',
                        () => isPositionValid() || 'Position must be at least 2 characters and less than 20 characters'
                    ]" :counter="20" label="Job Title"></v-text-field>
                </v-col>
            </v-row>
            <v-row no-gutters>
                <v-col>
                    <v-text-field class="pa-2" v-model="about.address" :rules="[
                        () => !!about.address || 'This field is required',
                        () => isAddressValid() || 'Address must be less than 50 characters'
                    ]" :counter="50" label="Address"></v-text-field>
                </v-col>
            </v-row>
            <v-row no-gutters>
                <v-text-field class="pa-2" v-model="about.description" :rules="[
                    () => !!about.description || 'This field is required',
                    () => isDescriptionValid() || 'Introduction must be less than 250 characters'
                ]" :counter="250" label="Introduction"></v-text-field>
            </v-row>
            <div class="d-flex justify-center">
                <form @submit.prevent="uploadImage">
                    <input type="file" @change="handleFileChange" accept="image/png">
                    <v-btn color = "light-blue-darken-1" class="ml-5" @click="upload(about)"
                        >Upload IMG
                        <v-icon 
                            size="x-large"
                            icon="mdi-upload"
                        ></v-icon>
                    </v-btn>
                </form>
                <!-- Image Upload and Cropper Dialog -->
                <v-dialog v-model="cropperDialog" max-width="500px">
                    <v-card>
                        <v-card-title>Crop Image</v-card-title>
                        <v-card-text>
                            <vue-cropper ref="cropperRef" :src="selectedImageUrl" :aspect-ratio="1"
                                style="width: 100%;"></vue-cropper>
                        </v-card-text>
                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn color="primary" @click="cropImage">Crop</v-btn>
                            <v-btn color="primary" text @click="cropperDialog = false">Cancel</v-btn>
                        </v-card-actions>
                    </v-card>
                </v-dialog>
                <v-btn color="green" class="ml-5" @click="saveAbout(about)">Save
                    <v-icon size="x-large" icon="mdi-content-save"></v-icon>
                </v-btn>
            </div>
        </v-expansion-panel-text>
    </v-expansion-panel>
</template>

<script>
import { ref, watch, computed } from 'vue';
import VueCropper from 'vue-cropperjs';
import 'cropperjs/dist/cropper.css';

export default {
    props: ["about"],
    components: {
        VueCropper,
    },
    setup(props, { emit }) {
        // Watch for changes in 'skills' prop
        // watch(() => props.about, (newAbout, oldAbout) => {
        //   console.log('New value:', newAbout);
        //   console.log('Old value:', oldAbout);
        // });
        const selectedFile = ref(null);
        const selectedImageUrl = ref(null);
        const cropperDialog = ref(false);
        const cropperRef = ref(null)

        const handleFileChange = (event) => {
            const file = event.target.files[0];
            if (file && file.type.includes('image')) {
                selectedFile.value = file;
                selectedImageUrl.value = URL.createObjectURL(file);
                cropperDialog.value = true;
            } else {
                alert('Please select an image file.');
            }
        };

        const cropImage = () => {
            if (cropperRef.value && cropperRef.value.cropper) {
                const cropper = cropperRef.value.cropper;
                const croppedCanvas = cropper.getCroppedCanvas();

                // Determine the original file type (default to 'image/png' if unknown)
                const originalFileType = selectedFile.value && selectedFile.value.type ? selectedFile.value.type : 'image/png';

                // Convert canvas to Blob in the original file type
                croppedCanvas.toBlob((blob) => {
                    const croppedImageUrl = URL.createObjectURL(blob);
                    selectedImageUrl.value = croppedImageUrl; // Update the selected image URL to the cropped image

                    // Save the blob for later upload, preserving the original file type
                    selectedFile.value = new File([blob], ".png", { type: originalFileType });

                    cropperDialog.value = false;
                }, originalFileType);
            } else {
                console.error('Cropper instance is not available');
            }
        };

        const isNameValid = () => {
            return !!props.about.name && props.about.name.length >= 2 && props.about.name.length <= 20;
        };
        const isPositionValid = () => {
            return !!props.about.role && props.about.role.length >= 2 && props.about.role.length <= 20;
        };
        const isAddressValid = () => {
            return !!props.about.address && props.about.address.length <= 50;
        };
        const isDescriptionValid = () => {
            return !!props.about.description && props.about.description.length <= 250;
        };
        const saveAbout = (about) => {

            let allRulesPassed = true;
            if (!isNameValid() ||
                !isPositionValid() ||
                !isAddressValid() ||
                !isDescriptionValid()) {
                allRulesPassed = false;
            }

            if (allRulesPassed) {
                // console.log('data format is correct')
                alert('Your About information has been saved!')
                emit('save-about', about);
            } else {
                confirm('Some fields may be incorrect. Please check!')
            }
        }

        const upload = (about) => {
            if (!selectedFile.value) {
                alert("Please select a file first.");
                return;
            }

            const formData = new FormData();
            formData.append('image', selectedFile.value);

            fetch('http://127.0.0.1:3033/upload', {
                method: 'POST',
                headers: {
                    Authorization: `Bearer ` + sessionStorage.getItem("access_token"),
                },
                body: formData,
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Upload successful:', data);
                    // Handle successful upload
                })
                .catch((error) => {
                    console.error('Upload error:', error);
                    // Handle upload error
                });
        };


        return {
            saveAbout,
            isNameValid,
            isPositionValid,
            isAddressValid,
            isDescriptionValid,
            handleFileChange,
            upload,
            selectedFile,
            selectedImageUrl,
            cropperDialog,
            cropperRef,
            handleFileChange,
            cropImage,
        };
    },

}
</script>

<style></style>


