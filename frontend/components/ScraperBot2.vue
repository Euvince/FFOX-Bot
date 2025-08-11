<template>
  <div class="min-h-screen bg-[#f5f5f5] py-10 px-4">
    <div class="max-w-5xl mx-auto bg-[#eeeeee] rounded-md shadow p-10">
      <h1 class="text-3xl font-semibold text-center text-white bg-[#5397d6] py-4 rounded-md mb-10">
        Archive Scraper Bot
      </h1>

      <form class="space-y-6">
        <div>
          <label class="block text-base text-gray-800 mb-1">Archive Url</label>
          <UInput v-model="archiveUrl" size="lg" color="white" class="border border-gray-400" />
        </div>
        <div>
          <label class="block text-sm text-gray-700 mb-1">Base Url</label>
          <p class="text-blue-600 text-sm">https://truecrimenews.com/</p>
        </div>
        <div>
          <label class="block text-base text-gray-800 mb-1">Next Page/Button Selector</label>
          <UInput v-model="nextPageSelector" size="lg" color="white" class="border border-gray-400" />
        </div>
        <div>
          <label class="block text-base text-gray-800 mb-1">Primary Keywords</label>
          <UInput v-model="primaryKeywords" placeholder="seperate multiple by ';'" size="lg" color="white" class="border border-gray-400" />
        </div>
        <div>
          <label class="block text-base text-gray-800 mb-1">Secondary Keywords</label>
          <UInput v-model="secondaryKeywords" placeholder="seperate multiple by ';'" size="lg" color="white" class="border border-gray-400" />
        </div>
        <div class="flex flex-col md:flex-row gap-6">
          <div class="flex-1">
            <label class="block text-base text-gray-800 mb-1">Date to start from</label>
            <UInput v-model="startDate" type="date" size="lg" color="white" class="border border-gray-400" />
          </div>
          <div class="flex-1">
            <label class="block text-base text-gray-800 mb-1">Date to end at</label>
            <UInput v-model="endDate" type="date" size="lg" color="white" class="border border-gray-400" />
          </div>
        </div>
        <div class="flex flex-col sm:flex-row gap-4 pt-6">
          <UButton color="blue" variant="solid">START BOT</UButton>
          <UButton color="blue" variant="outline">SHOW ALL RUNNING</UButton>
        </div>
      </form>
    </div>
  </div>
</template>


<script setup>
    const archiveUrl = ref('')
    const baseUrl = ref('https://truecrimenovs.com/')
    const nextPageSelector = ref('')
    const primaryKeywords = ref('')
    const secondaryKeywords = ref('')
    const startDate = ref('')
    const endDate = ref('')

    const startBot = () => {
    console.log('Starting bot with configuration:', {
        archiveUrl: archiveUrl.value,
        baseUrl: baseUrl.value,
        nextPageSelector: nextPageSelector.value,
        primaryKeywords: primaryKeywords.value,
        secondaryKeywords: secondaryKeywords.value,
        startDate: startDate.value,
        endDate: endDate.value
    })
    // Appel API pour déclencher une action
    }
</script>


<style>

</style>