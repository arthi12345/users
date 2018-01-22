$scope.checkHash = function(){
        $scope.openModalPopupOpen();
        //var gitHash = angular.isDefined($scope.pushGitHashkey) ? $scope.pushGitHashkey : "dummy"
        //$http.post("/ereconts_api/utilities/" + gitHash +"/hashInfo").success(function (data, status) {
            $http.post("/ereconts_api/utilities/dummy/hashInfo").success(function (data, status) {
            $scope.openModalPopupClose();
           $scope.showSuccessMessages(data.msg.output);
        }).error(function (err) {
            });
    }
