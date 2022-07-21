function ViewModel(url) {
  var self = this;
  self.ImageBase64 = ko.observable();
  self.ImageType = ko.observable();
  self.ImageSrcName = ko.computed(function () {
    return "data:" + self.ImageType() + "base64," + self.ImageBase64();
  });
  self.Detail = ko.observable();
  self.Update = function () {
    $.ajax(url, {
      type: "GET",
      dataType: "json",
      success: function (allData) {
        self.ImageBase64(allData.ImageBase64);
        self.ImageType(allData.ImageType);
        self.Detail(allData.Detail);
      },
    });
  };
}
