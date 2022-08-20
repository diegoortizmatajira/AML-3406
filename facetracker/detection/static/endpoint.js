function ViewModel(url) {
  var self = this;
  self.ImageBase64 = ko.observable();
  self.HistoricChartBase64 = ko.observable();
  self.PieChartBase64 = ko.observable();
  self.ImageType = ko.observable();
  self.ImageSrcName = ko.computed(function () {
    return "data:" + self.ImageType() + "base64," + self.ImageBase64();
  });
  self.PieChartSrcName = ko.computed(function () {
    return "data:" + self.ImageType() + "base64," + self.PieChartBase64();
  });
  self.HistoricChartSrcName = ko.computed(function () {
    return "data:" + self.ImageType() + "base64," + self.HistoricChartBase64();
  });
  self.Update = function () {
    $.ajax(url, {
      type: "GET",
      dataType: "json",
      success: function (allData) {
        self.ImageType(allData.ImageType);
        if (allData.ImageBase64)
          self.ImageBase64(allData.ImageBase64);
        if (allData.PieChartBase64)
          self.PieChartBase64(allData.PieChartBase64);
        if (allData.HistoricChartBase64)
          self.HistoricChartBase64(allData.HistoricChartBase64);
      },
    });
  };
}
