<template>
  <div class="min-h-screen bg-[#f5f5f5] py-10 px-4">
    <div class="max-w-5xl mx-auto bg-[#eeeeee] rounded-md shadow p-10">
      <h1 class="text-3xl font-semibold text-center text-white bg-[#5397d6] py-4 rounded-md mb-10">Archive Scraper Bot</h1>

      <form class="space-y-6">
        <div>
          <label class="block text-base text-gray-800 mb-1">Archive Url</label>
          <input type="text" v-model="archiveUrl" class="w-full px-4 py-2 border border-gray-400 rounded text-black" />
        </div>
        <div>
          <label class="block text-sm text-gray-700 mb-1">Base Url</label>
          <p class="text-blue-600 text-sm">https://truecrimenews.com/</p>
        </div>
        <div>
          <label class="block text-base text-gray-800 mb-1">HTML Content</label>
          <textarea type="text" rows="5" v-model="htmlContent" class="w-full px-4 py-2 border border-gray-400 rounded text-black" />
        </div>
        <div>
          <label class="block text-base text-gray-800 mb-1">Primary Keywords</label>
          <input type="text" v-model="primaryKeywords" placeholder="seperate multiple by ';'" class="w-full px-4 py-2 border border-gray-400 rounded text-black" />
        </div>
        <div>
          <label class="block text-base text-gray-800 mb-1">Secondary Keywords</label>
          <input type="text" v-model="secondaryKeywords" placeholder="seperate multiple by ';'" class="w-full px-4 py-2 border border-gray-400 rounded text-black" />
        </div>
        <div class="flex flex-col sm:flex-row gap-4 pt-6">
          <button
            @click="startBot"
            type="button" class="bg-[#4ba3e3] text-white px-6 py-2 rounded hover:bg-[#368acc] transition cursor-pointer"
          >
            START BOT
          </button>
        </div>
      </form>
    </div>
  </div>
</template>


<script setup>
    const archiveUrl = ref('')
    const baseUrl = ref('https://example.com/')
    const htmlContent = ref('')
    const primaryKeywords = ref('')
    const secondaryKeywords = ref('')

    const startBot = () => {
    console.log('Starting bot with configuration:', {
        archiveUrl: archiveUrl.value,
        baseUrl: baseUrl.value,
        htmlContent: htmlContent.value,
        primaryKeywords: primaryKeywords.value,
        secondaryKeywords: secondaryKeywords.value
    })
    // Appel API pour déclencher une action
    }
</script>


<style>

</style>